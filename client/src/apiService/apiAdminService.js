import axios from 'axios';
import {ref } from "vue";

const apiService = {
    async fetchData(resource) {
        const r =  await axios.get(`/api/${resource}/`);
        return r.data
    },
    async fetchFields(resource) {
        const f =  await axios.get(`/api/${resource}/fields/`);
        return f.data;
    },
    async takeChoices(dataFields) {
        const choices = ref({})
        dataFields.value.forEach((field) => {
            if (field.type == "choice" || field.type == "choiceList") {
                choices.value[field.name] = field.related_info.options;
            }
        });
        return choices.value;  
    },
    async delete(resource, id) {
        try {
            await axios.delete(`/api/${resource}/${id}/`);
            await fetchData();
        } catch (error) {
            console.log(error);
        }
    },

    async create(resource, formData) {
        await axios.post(`/api/${resource}/`, formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        });
    },

    async edit(resource, id, formData) {
        try {
            await axios.put(
                `/api/${resource}/${id}/`,
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );
        } catch (error) {
            console.error("Ошибка при обновлении записи:", error);
        }
    },
};
export default apiService;


