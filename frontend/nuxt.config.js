export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  ssr: false,
  head: {
    title: 'Siap Ujian',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/assets/scss/style.scss'
  ],
  rules: [{
    test: /\.scss$/,
    use: [{
      loader: "vue-style-loader"
    }, {
      loader: "css-loader", options: {
        sourceMap: true
      }
    }, {
      loader: "sass-loader", options: {
        sourceMap: true
      }
    }, {
      loader: "less-loader", options: {
        sourceMap: true
      }
    }]
  }],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    '~/plugins/vue-loading.js'
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: '/',
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  loading: {
    color: '#008FD7',
    height: '3px'
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
