<script setup>
import { computed, onBeforeMount, ref } from "vue";
import axios from "axios";
import Cookies from "js-cookie";
onBeforeMount(() => {
  axios.defaults.headers.common["X-CSRFToken"] = Cookies.get("csrftoken");
});

const dataItemToAdd = ref({});
const data = ref([]);
const dataFields = ref([]);
const dataItemToEdit = ref({});

const showModal = ref(false);
const showModalImage = ref(false);

const choices = ref({});

const dataImageUpdateShow = ref();
const dataImageUpdateSave = ref();

const dataItemImageEditSave = ref();
const dataItemImageEditShow = ref();

const modalImage = ref();

const handleFileUpload = (event) => {
  dataImageUpdateSave.value = event.target.files[0];
  dataImageUpdateShow.value = URL.createObjectURL(event.target.files[0]);
};

const handleFileEdit = (event) => {
  dataItemImageEditSave.value = event.target.files[0];
  dataItemImageEditShow.value = URL.createObjectURL(event.target.files[0]);
  dataItemToEdit.value.picture = URL.createObjectURL(event.target.files[0]);
};

async function onModalImage(item) {
  if(showModalImage.value === false){
    showModalImage.value = true;
    modalImage.value = item
  }  
  else {
    showModalImage.value = false
  }
}

async function fetchData() {
  try {
    const r = await axios.get("/api/lessonNames/");
    data.value = r.data;
    const f = await axios.get("/api/lessonNames/fields/");
    dataFields.value = f.data;
    console.log(dataFields.value)
    dataFields.value.forEach((field) => {
      if (field.type == "choice") {
        choices.value[field.name] = field.related_info.options;
      }
    });
    console.log(choices.value);
  } catch (error) {
    console.log(error);
  }
}

async function onRemoveClick(student) {
  try {
    await axios.delete(`/api/lessonNames/${student.id}/`);
    await fetchData();
  } catch (error) {
    console.log(error);
  }
}

async function onDataItemAddClick() {
  const formData = new FormData();
  Object.entries(dataItemToAdd.value).forEach(([key, value]) => {
    formData.set(key, value);
  });
  formData.append("picture", dataImageUpdateSave.value);
  console.log("post post post post");
  await axios.post("/api/lessonNames/", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  await fetchData();
}

async function onDataItemEditClick() {
  const formData = new FormData();
  Object.entries(dataItemToEdit.value).forEach(([key, value]) => {
    formData.set(key, value);
  });
  formData.append("picture", dataItemImageEditSave.value);
  console.log("lessonImageEditSave.value");
  console.log(dataItemImageEditSave.value);
  console.log("lessonImageEditSave.value");
  try {
    showModal.value = false;
    await axios.put(
      `/api/lessonNames/${dataItemToEdit.value.id}/`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

    await fetchData();
  } catch (error) {
    console.error("Ошибка при обновлении записи:", error);
  }
}

async function onLoadClick(item) {
  await fetchData();
}

function openModal(item) {
  showModal.value = true;
  dataItemImageEditShow.value = item.picture;
  dataItemToEdit.value = item;
}

function closeModal() {
  showModal.value = false;
}

onBeforeMount(async () => {
  await fetchData();
});
</script>




<template>
  <div>
    <!-- ТУТ ПОДКЛЮЧИЛ обработчик отправки формы -->
    <div class="edit-frame">
      <form >
        <div class="row">
          <div class="col">
            <div class="form-floating">
              <div
                v-for="item in dataFields"
                :key="item.id"
                class="student-item"
              >
                <div class="flex-container">
                  <div class="item-2-3-edit">
                    <template v-if="item.type === 'choice'">
                      <select
                        class="form-select"
                        v-model="dataItemToAdd[item.name]"
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

                    <template v-else-if="item.type === 'FileField'">
                      <input
                        type="file"
                        class="form-control"
                        @change="handleFileUpload"
                        required
                      />

                      <img
                        :src="dataImageUpdateShow"
                        alt="Предварительный просмотр"
                        style="max-height: 100px"
                      />
                    </template>
                    <template v-else>
                      <input
                        type="text"
                        class="form-control"
                        v-model="dataItemToAdd[item.name]"
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
          <button class="btn btn-primary" @click="onDataItemAddClick"> Добавить</button>
        </div>
      </form>
    </div>

    <div class="edit-frame">
      <div v-for="item in data" :key="item.id" class="student-item">
        <div>{{ item.name }}</div>
        <div v-show="item.picture">
          <button class="imageModalBtn" @click="onModalImage(item.picture)">
            <img :src="item.picture" style="max-height: 60px" />
          </button>
        </div>

        <button
          class="btn btn-success"
          @click="openModal(item)"
          data-bs-toggle="modal"
          data-bs-target="#editStudentModal"
        >
          <i class="bi bi-pen-fill"></i>
        </button>
        <button class="btn btn-danger" @click="onRemoveClick(item)">
          <i class="bi bi-x-lg"></i>
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
              <form @submit.prevent.stop="onDataItemEditClick">
                <div class="row">
                  <div class="col">
                    <div class="form-floating">
                      <div
                        v-for="item in dataFields"
                        :key="item.id"
                        class="student-item"
                      >
                        <div class="flex-container">
                          <div class="item-2-3-edit">
                            <template v-if="item.type === 'choice'">
                              <select
                                class="form-select"
                                v-model="dataItemToEdit[item.name]"
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
                            <template v-else-if="item.type === 'FileField'">
                              <input
                                type="file"
                                class="form-control"
                                @change="handleFileEdit"
                                required
                              />
                              <img
                                :src="dataItemToEdit.picture"
                                alt="Предварительный просмотр"
                                style="max-height: 100px"
                              />
                            </template>
                            <template v-else>
                              <input
                                type="text"
                                class="form-control"
                                v-model="dataItemToEdit[item.name]"
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

    <div
      v-if="showModalImage"
      class="modal fade show"
      tabindex="-1"
      style="display: block"
      role="dialog"
    >
      <!-- Full screen modal -->
      <div class="modal-dialog modal-lg">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Modal title</h5>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div class="modal-body">
              <img :src="modalImage" alt="">
            </div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
                @click="onModalImage"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Фон модального окна -->
    <div
      v-if="showModal || showModalImage"
      class="modal-backdrop fade show"
    ></div>
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
.imageModalBtn {
  background-color: transparent;
  border-color: transparent;
}
</style>
