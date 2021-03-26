import { create } from 'apisauce'

const api = create({
    baseURL: 'http://localhost:8000/api/v1/',
})

api.addRequestTransform(request => {
    const token = localStorage.getItem('token')
    if (token) {
        request.headers.Authorization = `Bearer ${token}`
    } 
})

api.axiosInstance.interceptors.response.use(response => {
    // 2xx response 
    return response;
}, async function (error) {
    // not 2xx response
    // removing and refreshing token when invalid
    if (error.response.status === 401) {
        localStorage.removeItem('token');

        const refresh = localStorage.getItem('refresh')

        if (refresh) {
            const response = await api.post('token/refresh/',{
                refresh: refresh
            })

            if (response.ok) {
                localStorage.setItem('token', response.data.access)
                error.config.headers.Authorization = `Bearer ${response.data.access}`
                return api.axiosInstance(error.config)
            } 

            else {
                localStorage.removeItem('refresh')
                window.location = '/'
            }
        }
    }
    
    return Promise.reject(error);
});

export default api