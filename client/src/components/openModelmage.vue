<script setup>
import {defineEmits, reactive, ref } from "vue";
import _ from "lodash";
const props = defineProps({
  modalImage: {
    type: String,
    required: true,
  }
});
const emit = defineEmits(["closeModalImage"]);
async function closeModalImage() {
    emit("closeModalImage")
}
</script>
<template>
  <div
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
            <h5 class="modal-title"></h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
              @click="closeModalImage"
            ></button>
          </div>
          <div class="modal-body">
            <img :src="props.modalImage" alt="" />
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