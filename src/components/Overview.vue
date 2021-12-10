<template>
  <div>
    <h1 class="glow">Advent of Code</h1>
    <b-button>
      <div class="tree" v-html="this.tree"></div>
      <h4 class="year-text">{:year <span class="glow">2021</span>}</h4>
    </b-button>
    <b-button>
      <div class="tree" v-html="this.hat"></div>
      <h4 class="year-text">{:year <span class="glow">2020</span>}</h4>
    </b-button>
  </div>

</template>

<script>
export default {
  name: 'HelloWorld',
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
  font-family: "Source Code Pro", monospace;

}

.btn {
  width: 20em;
  height: 25em;;
  background: #0f0f23;
  margin: 1em;
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
  font-family: "Source Code Pro", monospace;
}

.center {
  margin-top: auto;
  margin-bottom: auto;
}

.card {
  width: 20em;
  height: 23em;;
  background: #0f0f23;
  border-color: white;
  margin-left: auto;
  margin-right: auto;
  float: none;
  margin-top: 10em;

}

.glow {
  color: green;
  text-shadow: 0 0 15px green;
}
</style>
