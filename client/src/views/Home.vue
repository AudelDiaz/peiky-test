<template>
  <div class="">
    <StoreList msg="Listado de Tiendas"/>
  </div>
</template>

<script>
// @ is an alias to /src
import StoreList from '@/components/StoreList.vue'

export default {
  name: 'home',
  components: {
    StoreList: StoreList
  }
}
</script>
