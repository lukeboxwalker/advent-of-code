<template>
  <div>
    <div class="animate__animated animate__fadeInDown">
      <h1 class="glow">Advent of Code</h1>
      <h6><span class="year-text">0x0000{:/^</span><span class="glow">my soltuions</span><span
          class="year-text">$/}</span></h6>
    </div>
    <b-button class="y2020">
      <div class="tree" v-html="this.tree"></div>
      <h4 class="year-text">{:year <span class="glow">2021</span>}</h4>
    </b-button>
    <b-button class="y2021">
      <div class="tree" v-html="this.hat"></div>
      <h4 class="year-text">{:year <span class="glow">2020</span>}</h4>
    </b-button>
    <Snowf :amount="100" :size="5" :speed="1.5" :wind="0" :opacity="0.8"
           :swing="2" :image="null" :zIndex="-1" :resize="true" color="#fff"
    ></Snowf>
  </div>
</template>

<script>
import Snowf from 'vue-snowf';

export default {
  name: 'HelloWorld',
  components: {
    Snowf
  },
  props: {
    msg: String
  },
  methods: {
    generate_ascii: function (strings, dict) {
      return strings.map(i => i.split("").map(x => {
        const c = x.split("")
        if (dict[c]) {
          return dict[c]
        } else {
          return c
        }
      }).reduce((acc, x) => acc.concat(x)))
          .map(x => '<p style="margin-bottom: 0">' + x + '</p>')
          .reduce((acc, x) => acc.concat(x))
    }
  },
  created() {
    const dict_tree = {
      "O": '<span style="color: dodgerblue">O</span>',
      "o": '<span style="color: orange">o</span>',
      "@": '<span style="color: darkred">@</span>',
      "꘎": '<span style="color: yellow">꘎</span>',
      ">": '&gt;',
      "<": '&lt;',
      "_": '<span style="color: saddlebrown">_</span>',
      "[": '<span style="color: saddlebrown">[</span>',
      "]": '<span style="color: saddlebrown">]</span>',
      "-": '<span style="color: yellow">-</span>',
      "|": '<span style="color: yellow">|</span>',
      "/": '<span style="color: yellow">/</span>',
      "\\": '<span style="color: yellow">\\</span>',
      " ": '&nbsp;'
    };
    const dict_hat = {
      "꘎": '<span style="color: yellow">꘎</span>',
      "~": '<span style="color: white">~</span>',
      ".": '<span style="color: white">.</span>',
      "(": '<span style="color: white">(</span>',
      ")": '<span style="color: white">)</span>',
      "-": '<span style="color: darkred">-</span>',
      "_": '<span style="color: darkred">_</span>',
      "|": '<span style="color: darkred">|</span>',
      "/": '<span style="color: darkred">/</span>',
      "\\": '<span style="color: darkred">\\</span>',
      '"': '<span style="color: white">"</span>',
      "'": '<span style="color: white">\'</span>',
      ",": '<span style="color: white">,</span>',
      "^": '<span style="color: white">^</span>',
      " ": '&nbsp;'
    };
    this.tree = this.generate_ascii([
      " ",
      "|",
      "\\|/",
      "--꘎--",
      ">o<",
      ">O<<<",
      ">>o>>꘎<",
      ">o<<<o<<<",
      ">>@>꘎<<O<<<",
      ">o>>@>>>o>o<<",
      ">꘎>>꘎<o<@<o<<<<",
      ">o>o<<<O<꘎>>꘎>>O<",
      "_ __] [__ _",
      " ",
    ], dict_tree)
    this.hat = this.generate_ascii([
      " ",
      " ",
      " ",
      "   _---_",
      "   / /  /\\|",
      "  /  / | \\ ꘎",
      "/   /  \\ \\",
      "/  /  / \\  \\",
      ".( ~~~~~~~~~~ ).",
      '( .",^. ~". " .~ )',
      "'~~~~~~~~~~~~~'",
      " ",
      " ",
      " ",
    ], dict_hat)
  },
}
</script>

<style lang="scss" scoped>

.year-text {
  color: #0b3d1a;
}

.y2021 {
  animation: fadeInRight;
  animation-duration: 2s;
}

.y2020 {
  animation: fadeInLeft;
  animation-duration: 2s;

}

.btn {
  width: 20em;
  height: 25em;;
  background: #0f0f23;
  margin: 2em;
}

.btn:hover {
  background: #0f0f23;
}

.btn:active {
  background: #0f0f23;
}

.tree {
  color: green;
  margin-top: 0;
  margin-bottom: 0;
}

.center {
  margin-top: auto;
  margin-bottom: auto;
}

.glow {
  color: green;
  text-shadow: 0 0 15px green;
}
</style>
