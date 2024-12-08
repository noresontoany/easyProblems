import apiService from './apiAdminService';
const resource = 'students';
export default {
    fetchData() {
        return apiService.fetchData(resource);
    },
    fetchFields() {
        return apiService.fetchFields(resource);
    },
    takeChoices(dataFields) {
        return apiService.takeChoices(dataFields);
    },
    delete(id) {
        return apiService.delete(resource, id);
    },
    create(data) {
        return apiService.create(data);
    },
    update(id) {
        return apiService.update(id);
    },
    edit(id, data) {
        return apiService.edit(id, data);
    },
};
