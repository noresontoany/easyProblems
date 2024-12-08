<script setup>
import { onBeforeMount, onMounted, ref, watch } from "vue";
import creteewItemPanel from "@/components/creteNewItemPanel.vue";
import listData from "@/components/listData.vue";
// import openModelEdit from "@/components/openModelEdit.vue";
import apiAdminService from "@/apiService/apiAdminService.js";
import Cookies from "js-cookie";
import axios from "axios";

const props = defineProps({
  resource: String,
  required: true,
});
watch(
  () => props.resource, 
  async (newResource) => {
    await allData(); 
  },
  { immediate: true }
);
const data = ref([]);
const dataFields = ref([]);
const choices = ref({});

onBeforeMount(() => {
  axios.defaults.headers.common["X-CSRFToken"] = Cookies.get("csrftoken");
});

async function allData() {
  data.value = await apiAdminService.fetchData(props.resource);
  dataFields.value = await apiAdminService.fetchFields(props.resource);
  choices.value = await apiAdminService.takeChoices(dataFields);
}

async function onLoadClick(item) {
  allData();
}

onBeforeMount(async () => {
  allData();
});

async function addItem(item) {
  const r = await apiAdminService.create(props.resource, item);
  allData();
}

async function onRemoveClick(id) {
  const r = await apiAdminService.delete(props.resource, id);
  allData();
}

async function onEditClick(id, formData) {
  const r = await apiAdminService.edit(props.resource, id, formData);
  allData();
}
</script>
<template>
  <div>
    <!-- {{ data }}<br><br><br>
    {{ dataFields }}<br><br><br>
    {{ choices }}<br><br><br> -->
    <creteewItemPanel
      @onDataItemAddClick="addItem"
      :dataFields="dataFields"
      :choices="choices"
    >
    </creteewItemPanel>
    <listData
      @onRemoveClick="onRemoveClick"
      @onModalEdit="onEditClick"
      :data="data"
      :dataFields="dataFields"
      :choices="choices"
    ></listData>
  </div>
</template>

<style scoped>
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
