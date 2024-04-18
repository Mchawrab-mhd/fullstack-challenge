import { createWebHistory, createRouter } from 'vue-router'
import DashboardPage from '../pages/DashboardPage.vue';
import LoginPage from '../pages/LoginPage.vue';
import MapsPage from '../pages/MapsPage.vue'

const routes = [
    { name: 'Login', path: '/login', component: LoginPage },
    { name: 'Dashboard', path: '/dashboard', component: DashboardPage },
    {name: 'MapsPage', path: '/maps/:id/:latitude/:longitude', component: MapsPage,props: true},
    { path: '/', redirect: () => {
        const userName = localStorage.getItem('userName');
        if (userName) {
            return '/dashboard'; // Redirect to dashboard if user name is found
        } else {
            return '/login'; // Redirect to login if user name is not found
        }
    }}
];
const router = Router()
export default router;

function Router() {
    const router = createRouter({
        history: createWebHistory(),
        routes,
    })
    return router;
}

