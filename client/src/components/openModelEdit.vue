<script setup>
import { reactive, ref } from "vue";
import _ from "lodash";
const props = defineProps({
  dataFields: {
    type: Array,
    required: true,
  },
  choices: {
    type: Object,
    required: true,
  },
  showModal: {
    type: Boolean,
    required: true,
  },
  dataItemToEdit: {
    type: Object,
    required: true,
  },
});

const dataItemImageEditShow = ref(props.dataItemToEdit.picture)
const emit = defineEmits(["closeModal", "onModelEditClick"]);

const localDataItemToEdit = ref({ ...props.dataItemToEdit });

const handleFileEdit = (event) => {
  localDataItemToEdit.value.picture = event.target.files[0];
  dataItemImageEditShow.value = URL.createObjectURL(
    localDataItemToEdit.value.picture
  );
};

async function onDataItemEditClick() {
  const formData = new FormData();
  Object.entries(localDataItemToEdit.value).forEach(([key, value]) => {
    formData.set(key, value);
  });
  console.log(localDataItemToEdit.value.picture);
  if (localDataItemToEdit.value.picture != undefined)
    formData.set("picture", localDataItemToEdit.value.picture);
  emit("onModelEditClick", props.dataItemToEdit.id, formData);
}
</script>
<template>


  
  <div
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
            @click="emit('closeModal')"
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
                              v-model="localDataItemToEdit[item.name]"
                              required
                            >
                              <option
                                :key="option.id"
                                :value="option.id"
                                v-for="option in choices[item.name]"
                              >
                                {{ option.verbose.slice(0, 20) }}
                              </option>
                            </select>
                          </template>
                          <template v-else-if="item.type === 'choiceList'">
                            <select
                              class="form-select"
                              v-model="localDataItemToEdit[item.name]"
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
                            />

                            <img
                              :src="dataItemImageEditShow"
                              alt="Предварительный просмотр"
                              style="max-height: 100px"
                            />
                          </template>
                          <template v-else>
                            <input
                              type="text"
                              class="form-control"
                              v-model="localDataItemToEdit[item.name]"
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