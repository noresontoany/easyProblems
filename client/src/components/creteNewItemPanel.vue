<script setup>
import { ref, watch } from "vue";

const props = defineProps({
  dataFields: {
    type: Array,
    required: true,
  },
  choices: {
    type: Object,
    required: true,
  },
});

// function clearFilters() {
//   document.querySelectorAll('input[type="text"]').forEach((input) => {
//     input.value = "";
//   });
// }

// watch(
//   () => props.dataFields,
//   (newData) => {
//     filterData.value = [...newData];
//     filters.value = [];
//     clearFilters();
//   },
//   { deep: false },
//   { immediate: true }
// );

const emit = defineEmits(["onDataItemAddClick"]);

const dataItemToAdd = ref({});
const dataImageUpdateShow = ref();

async function onDataItemAddClick() {
  const formData = new FormData();
  Object.entries(dataItemToAdd.value).forEach(([key, value]) => {
    formData.set(key, value);
  });
  console.log(formData);

  if (dataItemToAdd.value.picture != undefined)
    formData.append("picture", dataItemToAdd.value.picture);
  emit("onDataItemAddClick", formData);
}
const handleFileUpload = (event) => {
  dataItemToAdd.value.picture = event.target.files[0];
  dataImageUpdateShow.value = URL.createObjectURL(event.target.files[0]);
};
</script>

<template>
  <div>
    <div class="edit-frame">
      <form @submit.prevent.stop="onDataItemAddClick">
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
                    <template v-else-if="item.type === 'choiceList'">
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
                      />

                      <img
                        :src="dataImageUpdateShow"
                        alt="Предварительный просмотр"
                        style="max-height: 100px"
                      />
                    </template>
                    <template v-else-if="item.verbose == 'code'">
                      <textarea
                        type="text"
                        cols="40"
                        rows="5"
                        class="form-control"
                        v-model="dataItemToAdd[item.name]"
                        required
                      />
                      {{ item.name }}
                    </template>
                    <template v-else>
                      <input
                        type="text"
                        maxlength="13"
                        class="form-control"
                        v-model="dataItemToAdd[item.name]"
                        required
                      />
                      {{ item.name }}
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
</style>