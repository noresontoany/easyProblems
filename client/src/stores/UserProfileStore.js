import { defineStore } from "pinia";
import axios from "axios";
import { onBeforeMount, ref } from "vue";
const useUserProfile = 
defineStore("UserProfileStore", ()=>{
    const is_authenticated = ref();
    const username = ref();
    const is_superuser = ref();

    onBeforeMount(async ()=>{
        const r = await axios.get("/api/user/info/")
        is_authenticated.value = r.data.is_authenticated
        username.value = r.data.username
        is_superuser.value = r.data.is_superuser

    })
    return {is_authenticated, username, is_superuser}
    
})
export default useUserProfile