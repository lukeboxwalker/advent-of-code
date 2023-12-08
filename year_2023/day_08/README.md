
<h1>Day 8: Haunted Wasteland 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2023/day/8>Link to Day 8</a><h2>Part One 🎁</h2><p>You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about <b>ghosts</b> a few minutes ago.</p>
<p>One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of <b>network</b> of labeled nodes.</p>
<p>It seems like you're meant to use the <b>left/right</b> instructions to <b>navigate the network</b>. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!</p>
<p>After examining the maps for a bit, two nodes stick out: <code>AAA</code> and <code>ZZZ</code>. You feel like <code>AAA</code> is where you are now, and you have to follow the left/right instructions until you reach <code>ZZZ</code>.</p>
<p>This format defines each <b>node</b> of the network individually. For example:</p>
<pre><code>RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
</code></pre>
<p>Starting with <code>AAA</code>, you need to <b>look up the next element</b> based on the next left/right instruction in your input. In this example, start with <code>AAA</code> and go <b>right</b> (<code>R</code>) by choosing the right element of <code>AAA</code>, <code><b>CCC</b></code>. Then, <code>L</code> means to choose the <b>left</b> element of <code>CCC</code>, <code><b>ZZZ</b></code>. By following the left/right instructions, you reach <code>ZZZ</code> in <code><b>2</b></code> steps.</p>
<p>Of course, you might not find <code>ZZZ</code> right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: <code>RL</code> really means <code>RLRLRLRLRLRLRLRL...</code> and so on. For example, here is a situation that takes <code><b>6</b></code> steps to reach <code>ZZZ</code>:</p>
<pre><code>LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
</code></pre>
<p>Starting at <code>AAA</code>, follow the left/right instructions. <b>How many steps are required to reach <code>ZZZ</code>?</b></p>

<p>To begin, <a href="8/input" target="_blank">get your puzzle input</a>.</p>
<form method="post" action="8/answer"><input type="hidden" name="level" value="1"/><p>Answer: <input type="text" name="answer" autocomplete="off"/> <input type="submit" value="[Submit]"/></p></form>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://twitter.com/intent/tweet?text=%22Haunted+Wasteland%22+%2D+Day+8+%2D+Advent+of+Code+2023&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2023%2Fday%2F8&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' && ms.length){this.href='https://'+ms+'/share?text=%22Haunted+Wasteland%22+%2D+Day+8+%2D+Advent+of+Code+2023+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2023%2Fday%2F8';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
