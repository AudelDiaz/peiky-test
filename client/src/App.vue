<template>
    <div id="app">
        <nav>
            <div class="nav-wrapper yellow accent-4">
                <router-link to="/" class="brand-logo"><img class="logo" alt="Vue logo" src="./assets/logo.png">
                </router-link>
                <a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons">menu</i></a>
                <ul class="right hide-on-med-and-down">
                    <li>
                        <router-link class="red-text" to="/">Home</router-link>
                    </li>
                    <li>
                        <router-link class="red-text" to="/about">About</router-link>
                    </li>
                    <li>
                        <router-link to="/cart" class="orange">
                            Cart <span class="badge new red white-text">{{ getCartItems }}</span>
                        </router-link>
                    </li>
                </ul>
            </div>
        </nav>
        <div class="container">
            <router-view/>
        </div>

    </div>
    </div>
</template>

<script>

    export default {
        name: 'app',
        computed: {
            getCartItems() {
                return this.$store.getters.cartItemsCount;
            }
        }
    }
</script>

<style>
    .logo {
        height: 62px;
    }

    span.badge.new::after {
        content: " Products" !important;
    }
</style>
