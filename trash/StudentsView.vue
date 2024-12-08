<script setup>
import { computed, onBeforeMount, ref } from "vue";
import axios from "axios";
import Cookies from "js-cookie";

onBeforeMount(() => {
  axios.defaults.headers.common["X-CSRFToken"] = Cookies.get("csrftoken");
});

const studentToAdd = ref({});
const students = ref([]);
const sdtudentFields = ref([]);
const showModal = ref(false);
const studentToEdit = ref({});

async function fetchStudents() {
  try {
    const r = await axios.get("/api/students/");
    console.log((await r).data);
    students.value = r.data;
    const f = await axios.get("/api/students/fields");
    sdtudentFields.value = f.data;
    sdtudentFields.value.forEach((field) => {
      studentToAdd.value[field.name] = ""; 
      studentToEdit.value[field.name] = ""; 
    });
    // console.log(f.data);


    
  } catch (error) {
    console.log(error);
  }
}

async function onRemoveClick(student) {
  try {
    await axios.delete(`api/students/${student.id}/`);
    await fetchStudents();
  } catch (error) {
    console.log(error);
  }
}

async function onStudentAddClick() {
  await axios.post("/api/students/", {
    ...studentToAdd.value,
  });
  await fetchStudents();
}

async function onStudentUpdateClick() {
  try {
    showModal.value = false;
    await axios.put(`/api/students/${studentToEdit.value.id}/`, {
      ...studentToEdit.value, 
    });
    await fetchStudents();
  } catch (error) {
    console.error("Ошибка при обновлении записи:", error);
  }
  
}

async function onLoadClick(item) {
  await fetchStudents();
}

function openModal(item) {
  showModal.value = true;
  studentToEdit.value = item;
  // console.log(studentToEdit)
}

function closeModal() {
  showModal.value = false;
}

onBeforeMount(async () => {
  await fetchStudents();
});
</script>



<template>
  <div>
    <!-- ТУТ ПОДКЛЮЧИЛ обработчик отправки формы -->
    <div class="edit-frame">
      <form @submit.prevent.stop="onStudentAdd">
        <div class="row">
          <div class="col">
            <div class="form-floating">
              <div
                v-for="item in sdtudentFields"
                :key="item.id"
                class="student-item"
              >
                <div class="flex-container">
                  <div class="item-2-3-edit">
                    <input
                      type="text"
                      class="form-control"
                      v-model="studentToAdd[item.name]"
                      required
                    />
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
          <button class="btn btn-primary" @click="onStudentAddClick()">
            Добавить
          </button>
        </div>
        <div></div>
      </form>
    </div>
    <div class="edit-frame">
      <div v-for="item in students" :key="item.id" class="student-item">
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
              <form @submit.prevent.stop="onStudentAdd">
                <div class="row">
                  <div class="col">
                    <div class="form-floating">
                      <div
                        v-for="item in sdtudentFields"
                        :key="item.id"
                        class="student-item"
                      >
                        <div class="flex-container">
                          <div class="item-2-3-edit">
                            <input
                              type="text"
                              class="form-control"
                              v-model="studentToEdit[item.name]"
                              required
                            />
                          </div>
                          <div class="item-1-3-edit">
                            <label class for="floatingInput">{{
                              item.verbose
                            }} {{}}</label>

                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-auto"></div>
                <div class="col-auto">
                  <button
                    class="btn btn-primary"
                    @click="onStudentUpdateClick()"
                  >
                    Добавить
                  </button>
                </div>
                <div></div>
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

