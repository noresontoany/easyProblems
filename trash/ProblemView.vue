<script setup>
import { computed, onBeforeMount, ref } from "vue";
import axios from "axios";
import Cookies from "js-cookie";
import { storeToRefs } from "pinia";
import useUserProfile from "../stores/UserProfileStore";
const userProfile = useUserProfile();

const {
  is_authenticated,
  username,
  is_superuser
} = storeToRefs(userProfile)


 
onBeforeMount(() => {
  axios.defaults.headers.common["X-CSRFToken"] = Cookies.get("csrftoken");
});

const submissionToAdd = ref({});
const problems = ref([]);
const problemsFields = ref([]);
const showModal = ref(false);
const submissionToEdit = ref({});
const choices = ref({});

async function fetchproblems() {

  console.log("userProfile")
  console.log(is_authenticated)

  console.log("userProfile")  

  try {
    const r = await axios.get("/api/problems/");
    problems.value = r.data;
    console.log(r.data)
    const f = await axios.get("/api/problems/fields/");
    problemsFields.value = f.data;

    problemsFields.value.forEach((field) => {
      if (field.type == "choice") {
        choices.value[field.name] = field.related_info.options
      }
    });
    console.log(choices.value)
  } catch (error) {
    console.log(error);
  }
}

async function onRemoveClick(student) {
  try {
    await axios.delete(`/api/problems/${student.id}/`);
    await fetchproblems();
  } catch (error) {
    console.log(error);
  }
}

async function onLessonNameAddClick() {
  console.log("submissionToAdd.value add");
  console.log(submissionToAdd.value);
  await axios.post("/api/problems/", {
    ...submissionToAdd.value,
  });
  await fetchproblems();
}

async function onLessonNameEditClick() {
  try {
    showModal.value = false;
    await axios.put(`/api/problems/${submissionToEdit.value.id}/`, {
      ...submissionToEdit.value,
    });
    await fetchproblems();
  } catch (error) {
    console.error("Ошибка при обновлении записи:", error);
  }
}

async function onLoadClick(item) {
  await fetchproblems();
}

function openModal(item) {
  showModal.value = true;
  submissionToEdit.value = item;
}

function closeModal() {
  showModal.value = false;
}

onBeforeMount(async () => {
  await fetchproblems();
});
</script>



<template>
  <div>
    <!-- ТУТ ПОДКЛЮЧИЛ обработчик отправки формы -->
    <div class="edit-frame">
      <form @submit.prevent.stop="onLessonNameAddClick">
        <div class="row">
          <div class="col">
            <div class="form-floating">
              <div
                v-for="item in problemsFields"
                :key="item.id"
                class="student-item"
              >
                <div class="flex-container">
                  <div class="item-2-3-edit">
                    <template v-if="item.type === 'choice'">
                      <select
                        class="form-select"
                        v-model="submissionToAdd[item.name]"
                        required
                      >
                        <option
                          :key="option.id"
                          :value="option.id"
                          v-for="option in choices[item.name]"
                        >
                          {{ option.verbose }}
                        </option>
                      </select>
                    </template>
                    <template v-else>
                      <input
                        type="text"
                        class="form-control"
                        v-model="submissionToAdd[item.name]"
                        required
                      />
                    </template>
                  </div>
                  <div class="item-1-3-edit">
                    <label class for="floatingInput">{{ item.verbose }}</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-auto"></div>
        <div class="col-auto">
          <button class="btn btn-primary">Добавить</button>
        </div>
      </form>
    </div>
    <div class="edit-frame">
      <div v-for="item in problems" :key="item.id" class="student-item">
        <div>{{ item.name }}</div>
        <button
          class="btn btn-success"
          @click="openModal(item)"
          data-bs-toggle="modal"
          data-bs-target="#editStudentModal"
        >
          <i class="bi bi-pen-fill"></i>
        </button>
        <button class="btn btn-danger" @click="onRemoveClick(item)">
          <i class="bi bi-x"></i>
        </button>
      </div>
    </div>

    <div
      v-if="showModal"
      class="modal fade show"
      tabindex="-1"
      style="display: block"
      role="dialog"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Изменить запись</h5>
            <button
              type="button"
              class="btn-close"
              aria-label="Close"
              @click="closeModal"
            ></button>
          </div>
          <div class="modal-body">
            <div class="edit-frame">
              <form @submit.prevent.stop="onLessonNameEditClick">
                <div class="row">
                  <div class="col">
                    <div class="form-floating">
                      <div
                        v-for="item in problemsFields"
                        :key="item.id"
                        class="student-item"
                      >
                        <div class="flex-container">
                          <div class="item-2-3-edit">
                            <template v-if="item.type === 'choice'">
                              <select
                                class="form-select"
                                v-model="submissionToEdit[item.name]"
                                required
                              >
                                <option
                                  :key="option.id"
                                  :value="option.id"
                                  v-for="option in choices[item.name]"
                                >
                                  {{ option.verbose }}
                                </option>
                              </select>
                            </template>
                            <template v-else>
                              <input
                                type="text"
                                class="form-control"
                                v-model="submissionToEdit[item.name]"
                                required
                              />
                            </template>
                          </div>
                          <div class="item-1-3-edit">
                            <label class for="floatingInput">{{
                              item.verbose
                            }}</label>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-auto"></div>
                <div class="col-auto">
                  <button class="btn btn-primary">Добавить</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Фон модального окна -->
    <div v-if="showModal" class="modal-backdrop fade show"></div>
  </div>

  <!-- </div> -->
</template>

<style lang="scss" scoped>
.student-item {
  padding: 0.5rem;
  margin: 0.5rem 0;
  border: 1px solid silver;
  border-radius: 8px;
  display: grid;
  grid-template-columns: 1fr auto auto auto;
  align-content: center;
  align-items: center;
  gap: 16px;
}

.flex-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.item-2-3-edit {
  flex: 2;
  padding: 10px;
  color: black;
}

.item-1-3-edit {
  flex: 1;
  padding: 10px;
  color: black;
  text-align: right;
}

.edit-frame {
  border: 1px solid black;
  margin: 10px;
  border-radius: 8px;
  padding: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

/* Дополнительные стили для меток */
label {
  color: black;
  margin-left: 10px;
  font-weight: bold;
}

.modal-backdrop {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(1.5rem);
}
</style>
