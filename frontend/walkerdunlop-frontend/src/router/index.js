import { createWebHistory, createRouter } from 'vue-router'

import DashboardPage from '../pages/DashboardPage.vue';
import LoginPage from '../pages/LoginPage.vue';

const routes = [
    { name: 'Login', path: '/login', component: LoginPage },
    { name: 'Dashboard', path: '/dashboard', component: DashboardPage },
    { path: '/', redirect: () => {
        const userName = localStorage.getItem('userName');
        if (userName) {
            return '/dashboard'; // Redirect to dashboard if user name is found
        } else {
            return '/login'; // Redirect to login if user name is not found
        }
    }},
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

