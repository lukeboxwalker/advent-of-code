
<h1>Day 3: Gear Ratios 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2023/day/3>Link to Day 3</a><h2>Part One 🎁</h2><p>You and the Elf eventually reach a <a href="https://en.wikipedia.org/wiki/Gondola_lift" target="_blank">gondola lift</a> station; he says the gondola lift will take you up to the <b>water source</b>, but this is as far as he can bring you. You go inside.</p>
<p>It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.</p>
<p>"Aaah!"</p>
<p>You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.</p>
<p>The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can <b>add up all the part numbers</b> in the engine schematic, it should be easy to work out which part is missing.</p>
<p>The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently <b>any number adjacent to a symbol</b>, even diagonally, is a "part number" and should be included in your sum. (Periods (<code>.</code>) do not count as a symbol.)</p>
<p>Here is an example engine schematic:</p>
<pre><code>467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
</code></pre>
<p>In this schematic, two numbers are <b>not</b> part numbers because they are not adjacent to a symbol: <code>114</code> (top right) and <code>58</code> (middle right). Every other number is adjacent to a symbol and so <b>is</b> a part number; their sum is <code><b>4361</b></code>.</p>
<p>Of course, the actual engine schematic is much larger. <b>What is the sum of all of the part numbers in the engine schematic?</b></p>

<p>To begin, <a href="3/input" target="_blank">get your puzzle input</a>.</p>
<form method="post" action="3/answer"><input type="hidden" name="level" value="1"/><p>Answer: <input type="text" name="answer" autocomplete="off"/> <input type="submit" value="[Submit]"/></p></form>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://twitter.com/intent/tweet?text=%22Gear+Ratios%22+%2D+Day+3+%2D+Advent+of+Code+2023&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2023%2Fday%2F3&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' && ms.length){this.href='https://'+ms+'/share?text=%22Gear+Ratios%22+%2D+Day+3+%2D+Advent+of+Code+2023+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2023%2Fday%2F3';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
