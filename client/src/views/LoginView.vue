<script setup>
import { onBeforeMount, defineEmits, reactive, ref } from "vue";
import apiAdminService from "@/apiService/apiAdminService";

const newUser = ref({})


async function createUser() {
  console.log(newUser.value)
  
}



</script>



<template>
  <form>
    <div class="form-group">
      <label for="exampleInputPassword1">Хендл</label>
      <input
        type="text"
        class="form-control"
        v-model = "newUser['name']"
        id="exampleInputPassword1"
        placeholder="qwerty123"
      />
    </div>
    <div class="form-group">
      <label for="exampleInputPassword1">ФИО</label>
      <input
        type="text"
        v-model = "newUser['description']"
        class="form-control"
        id="exampleInputPassword1"
        placeholder="Вася Пупин Дубин"
      />
    </div>
    <div class="form-group">
      <label for="exampleInputEmail1">Login</label>
      <input
        type="text"
        class="form-control"
        id="exampleInputEmail1"
        v-model = "newUser['username']"
        aria-describedby="emailHelp"
        placeholder="Enter login"
      />
      <small id="emailHelp" class="form-text text-muted"
        >We'll never share your email with anyone else.</small
      >
    </div>
    <div class="form-group">
      <label for="exampleInputPassword1">Password</label>
      <input
        type="password"
        class="form-control"
        v-model = "newUser['password']"
        id="exampleInputPassword1"
        placeholder="Password"
      />
    </div>
    
    <div class="form-group form-check">
      <input type="checkbox" class="form-check-input" id="exampleCheck1" />
      <label class="form-check-label" for="exampleCheck1">Check me out</label>
    </div>
    <button type="button" @click="createUser" class = "btn btn-primary">Submit</button>
  </form>
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