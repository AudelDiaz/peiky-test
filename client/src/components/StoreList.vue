<template>
    <div class="">
        <h1 class="center-align">{{ msg }}</h1>
        <hr class="small">
        <span class="center-align red-text text-accent-3" v-if="loading">Loading...</span>
        <div class="row" v-else>
            <div class="col s12 m6 l4" v-for="store in products" :key="store.id">
                <div class="card">
                    <div class="card-image">
                        <img :src=store.logo :alt=store.name>
                        <router-link :to="{name: 'store', params: { slug: store.slug }}"  class="btn-floating halfway-fab waves-effect waves-light red">
                            <i class="material-icons">home</i>
                        </router-link>
                    </div>
                    <div class="card-content">
                        <span class="card-title red-text text-accent-3">{{ store.name }}</span>
                        <p>{{ store.slogan }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: "StoreList",
        data() {
            return {
                products: null,
                loading: true,
                errored: false
            }
        },
        props: {
            msg: String
        },
        mounted: function () {
            axios.get('https://peiky-python.herokuapp.com/api/stores.json')
                .then(response => {
                    this.products = response.data.results;
                })
                .catch(error => {
                    alert(error);
                    this.errored = true;
                })
                .finally(() => this.loading = false)
        }
    }
</script>

<style scoped>

</style>