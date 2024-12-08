<script setup>
import { onBeforeMount, defineEmits, reactive, ref } from "vue";
import apiAdminService from "@/apiService/apiAdminService";

const props = defineProps({
  resource: String,
  required: true,
});

const data = ref([]);
const dataFields = ref([]);
const choices = ref({});

async function allData() {
  data.value = await apiAdminService.fetchData(props.resource);
  dataFields.value = await apiAdminService.fetchFields(props.resource);
  choices.value = await apiAdminService.takeChoices(dataFields);
}
onBeforeMount(async () => {
  allData();
});
async function onLoadClick(item) {
  allData();
}
function findVerobose(dict){
  dataFields.filter({
    
  })
  
  return "Asd"
}


</script>

<template>
  {{ data }}<br /><br /><br />
  {{ dataFields }}<br /><br /><br />
  {{ choices }}<br /><br /><br />

  <div class="edit-frame">
    <div>
      <div class="table-responsive">
        <table class="table table-bordered">
          <thead>
            <tr>
              <th scope="col">id</th>
              <template v-for="field in dataFields">
                <th scope="col">{{ field.verbose }}</th>
              </template>
              <th scope="col">Редактировать</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="elem in data" :key="elem.id">
              <th scope="row">{{ elem.id }}</th>
              <td v-for="item in dataFields" :key="item.id">
                <tempalate v-if="item.type == 'choice'">
                  {{ elem[item.name].name }}
                </tempalate>
                <tempalate v-else-if="item.name == 'picture'">
                  <button class="imageModalBtn">
                    <img :src="elem.picture" style="max-height: 60px" />
                  </button>
                </tempalate>
                
                <tempalate v-else>
                  {{ elem[item.name] }}
                </tempalate>
              </td>
              <button
                type="button"
                class="btn btn-success"
                data-bs-toggle="modal"
                data-bs-target="#editStudentModal"
              >
                <i class="bi bi-pen-fill">Изменить</i>
              </button>
              <button type="button" class="btn btn-danger">
                <i class="bi bi-x-octagon-fill"> Удалить </i>
              </button>
            </tr>
          </tbody>
        </table>
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