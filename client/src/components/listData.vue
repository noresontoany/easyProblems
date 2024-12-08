<script setup>
import { ref, computed, reactive, onBeforeMount, watch } from "vue";
import openModelEdit from "./openModelEdit.vue";
import openModelmage from "./openModelmage.vue";
import _ from "lodash";

const props = defineProps({
  data: {
    type: Array,
    required: true,
  },
  dataFields: {
    type: Array,
    required: true,
  },
  choices: {
    type: Object,
    required: true,
  },
});

const dataFields = computed(() => props.dataFields);
const data = computed(() => props.data);
const choices = computed(() => props.choices);

const showModal = ref(false);
const showModalImage = ref(false);
const dataItemToEdit = ref({});

const filters = ref([]);

const dataItemImageEditSave = ref();
const dataItemImageEditShow = ref();



const filterData = ref([]);

function clearFilters() {
  filters.value = [];
  document.querySelectorAll('input[type="text"]').forEach((input) => {
    input.value = "";
  });
}

watch(
  () => props.data,
  (newData) => {
    filterData.value = [...newData];
    filters.value = [];
    clearFilters();
  },
  { deep: false },
  { immediate: true }
);

const modalImage = ref();

const emit = defineEmits(["onRemoveClick", "onModalEdit"]);


async function onModal(item) {
  showModal.value = !showModal.value;
  if (showModal.value) dataItemToEdit.value = item;
}

async function onModalEdit(id, formData) {
  showModal.value = false;
  emit("onModalEdit", id, formData);
}

async function onModalImage(item) {
  if (showModalImage.value === false) {
    showModalImage.value = true;
    modalImage.value = item;
  } else {
    showModalImage.value = false;
  }
}

async function onModalImageClose() {
  showModalImage.value = false;
}

async function filter(name, type, filter) {
  console.log(type);
  if (filter.trim() === "") {
    filters.value = filters.value.filter((item) => item.name != name);
    if (filters.value.length == 0) {
      filterData.value = data.value;
    }
  } else {
    const existingFilter = filters.value.find((item) => item.name === name);
    if (existingFilter) {
      existingFilter.filter = filter;
    } else {
      filters.value.push({ name, type, filter });
    }

    if (filters.value.length > 0) {
      filterData.value = data.value.filter((item) => {
        return filters.value.every((filter) => {
          const itemValue = item[filter.name];
          if (filter.type === "choice") {
            return !item[filter.name].name.search(filter.filter)
          } else {
            return !itemValue.search(filter.filter); // Сравниваем значения
          }
        });
      });
    }
  }
  console.log(filters);
}
</script>
<template>
  <div class="edit-frame">
    <div>
      <div class="table-responsive">
        <table class="table table-bordered">
          <thead>
            <tr>
              <th scope="col">id</th>
                <th v-for="field in dataFields" :key="field.name" scope="col">
                  {{ field.verbose }}<br/><br/><br/>
                  <input v-if="field.name != 'picture'"
                    type="text"
                    id="search"
                    @input="filter(field.name, field.type, $event.target.value)"
                  />
                </th>
                <th scope="col">Редактировать</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="elem in filterData" :key="elem.id">
              <th scope="row">{{ elem.id }}</th>
              <td v-for="item in dataFields" :key="item.id">
                <tempalate v-if="item.type == 'choice'">
                  {{ elem[item.name].name }}
                </tempalate>
                <tempalate v-else-if="item.type == 'choiceList'">
                  {{ elem[item.name] }}
                </tempalate>
                <tempalate v-else-if="item.name == 'picture'">
                  <button
                    class="imageModalBtn"
                    @click="onModalImage(elem.picture)"
                  >
                    <img :src="elem.picture" style="max-height: 60px" />
                  </button>
                </tempalate>

                <tempalate v-else>
                  {{ elem[item.name] }}
                </tempalate>
              </td>
              <button
                class="btn btn-success"
                @click="onModal(elem)"
                data-bs-toggle="modal"
                data-bs-target="#editStudentModal"
              >
                <i class="bi bi-pen-fill">Изменить</i>
              </button>
              <button
                class="btn bt n-danger"
                @click="emit('onRemoveClick', elem.id)"
              >
                <i class="bi bi-x-octagon-fill"></i>
              </button>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-if="showModal">
      <openModelEdit
        @close-modal="onModal"
        @onModelEditClick="onModalEdit"
        :data-fields="dataFields"
        :choices="choices"
        :data="props.data"
        :show-modal="showModal"
        :data-item-to-edit="dataItemToEdit"
      />
    </div>
    <div v-if="showModalImage">
      <openModelmage
        @close-modal-image="onModalImageClose"
        :modal-image="modalImage"
      />
    </div>
    <div
      v-if="showModal || showModalImage"
      class="modal-backdrop fade show"
    ></div>
  </div>
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
.filterButton {
  background-color: transparent;
  border-color: transparent;
}
</style>