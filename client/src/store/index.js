import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        cart_items: [],
    },
    mutations: {
        addProduct(state, item) {
            state.cart_items.push(item);
        },
        removeProduct(state, item) {
            state.cart_items.splice(state.cart_items.indexOf(item), 1);
        },
        updateProduct(state, old, updated) {
            let index = state.cart_items.indexOf(old);
            if (index !== -1) {
                state.cart_items[index] = updated;
            }
        },
        cleanCart(state) {
            state.cart_items = []
        }
    },
    actions: {},
    getters: {
        cartItemsCount: (state) => {
            return state.cart_items.length
        },
        cartItems: (state) => {
            return state.cart_items
        },
        sumCartItems: (state) => {
            let items = state.cart_items;
            let sum = 0;
            for (let i = 0; i < items.length; i++) {
                sum += Number(items[i].price);
            }
            return sum;
        }
    }
})
