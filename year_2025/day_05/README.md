
<h1>Day 5: Cafeteria 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2025/day/5>Link to Day 5</a><h2>Part One 🎁</h2><p>As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.</p>
<p>You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.</p>
<p>"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.</p>
<p>The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are <b>fresh</b> and which are <span title="No, this puzzle does not take place on Gleba. Why do you ask?"><b>spoiled</b></span>. When you ask how it works, they give you a copy of their database (your puzzle input).</p>
<p>The database operates on <b>ingredient IDs</b>. It consists of a list of <b>fresh ingredient ID ranges</b>, a blank line, and a list of <b>available ingredient IDs</b>. For example:</p>
<pre><code>3-5
10-14
16-20
12-18

1
5
8
11
17
32
</code></pre>
<p>The fresh ID ranges are <b>inclusive</b>: the range <code>3-5</code> means that ingredient IDs <code>3</code>, <code>4</code>, and <code>5</code> are all <b>fresh</b>. The ranges can also <b>overlap</b>; an ingredient ID is fresh if it is in <b>any</b> range.</p>
<p>The Elves are trying to determine which of the <b>available ingredient IDs</b> are <b>fresh</b>. In this example, this is done as follows:</p>
<ul>
<li>Ingredient ID <code>1</code> is spoiled because it does not fall into any range.</li>
<li>Ingredient ID <code>5</code> is <b>fresh</b> because it falls into range <code>3-5</code>.</li>
<li>Ingredient ID <code>8</code> is spoiled.</li>
<li>Ingredient ID <code>11</code> is <b>fresh</b> because it falls into range <code>10-14</code>.</li>
<li>Ingredient ID <code>17</code> is <b>fresh</b> because it falls into range <code>16-20</code> as well as range <code>12-18</code>.</li>
<li>Ingredient ID <code>32</code> is spoiled.</li>
</ul>
<p>So, in this example, <b><code>3</code></b> of the available ingredient IDs are fresh.</p>
<p>Process the database file from the new inventory management system. <b>How many of the available ingredient IDs are fresh?</b></p>

<p class="day-success">The first half of this puzzle is complete! It provides one gold star: *</p>
<h2>Part Two 🎁</h2><p>The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.</p>
<p>So that they can stop bugging you when they get new inventory, the Elves would like to know <b>all</b> of the IDs that the <b>fresh ingredient ID ranges</b> consider to be <b>fresh</b>. An ingredient ID is still considered fresh if it is in any range.</p>
<p>Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:</p>
<pre><code>3-5
10-14
16-20
12-18
</code></pre>
<p>The ingredient IDs that these ranges consider to be fresh are <code>3</code>, <code>4</code>, <code>5</code>, <code>10</code>, <code>11</code>, <code>12</code>, <code>13</code>, <code>14</code>, <code>15</code>, <code>16</code>, <code>17</code>, <code>18</code>, <code>19</code>, and <code>20</code>. So, in this example, the fresh ingredient ID ranges consider a total of <b><code>14</code></b> ingredient IDs to be fresh.</p>
<p>Process the database file again. <b>How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?</b></p>

<form method="post" action="5/answer"><input type="hidden" name="level" value="2"/><p>Answer: <input type="text" name="answer" autocomplete="off"/> <input type="submit" value="[Submit]"/></p></form>
<p>Although it hasn't changed, you can still <a href="5/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+Part+One+of+%22Cafeteria%22+%2D+Day+5+%2D+Advent+of+Code+2025+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F5" target="_blank">Bluesky</a>
  <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+Part+One+of+%22Cafeteria%22+%2D+Day+5+%2D+Advent+of+Code+2025&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F5&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' && ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+Part+One+of+%22Cafeteria%22+%2D+Day+5+%2D+Advent+of+Code+2025+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F5';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
