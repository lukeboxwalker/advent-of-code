
<h1>Day 4: Printing Department 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2025/day/4>Link to Day 4</a><h2>Part One 🎁</h2><p>You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really <span title="This joke is stupid and I love it.">big</span> print jobs).</p>
<p>Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.</p>
<p>"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."</p>
<p>If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.</p>
<p>The rolls of paper (<code>@</code>) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.</p>
<p>For example:</p>
<pre><code>..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
</code></pre>
<p>The forklifts can only access a roll of paper if there are <b>fewer than four rolls of paper</b> in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.</p>
<p>In this example, there are <code><b>13</b></code> rolls of paper that can be accessed by a forklift (marked with <code>x</code>):</p>
<pre><code>..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
</code></pre>
<p>Consider your complete diagram of the paper roll locations. <b>How many rolls of paper can be accessed by a forklift?</b></p>

<h2>Part Two 🎁</h2><p>Now, the Elves just need help accessing as much of the paper as they can.</p>
<p>Once a roll of paper can be accessed by a forklift, it can be <b>removed</b>. Once a roll of paper is removed, the forklifts might be able to access <b>more</b> rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?</p>
<p>Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted <code><b>@</b></code> to indicate that a roll of paper is about to be removed, and using <code>x</code> to indicate that a roll of paper was just removed:</p>
<pre><code>Initial state:
..<b>@</b><b>@</b>.<b>@</b><b>@</b>@<b>@</b>.
<b>@</b>@@.@.@.@@
@@@@@.<b>@</b>.@@
@.@@@@..@.
<b>@</b>@.@@@@.@<b>@</b>
.@@@@@@@.@
.@.@.@.@@@
<b>@</b>.@@@.@@@@
.@@@@@@@@.
<b>@</b>.<b>@</b>.@@@.<b>@</b>.

Remove 13 rolls of paper:
..xx.xx<b>@</b>x.
x@@.<b>@</b>.<b>@</b>.@<b>@</b>
<b>@</b>@@@@.x.@@
<b>@</b>.@@@@..<b>@</b>.
x@.@@@@.<b>@</b>x
.<b>@</b>@@@@@@.<b>@</b>
.<b>@</b>.@.@.@@@
x.@@@.@@@@
.<b>@</b>@@@@@@@.
x.x.@@@.x.

Remove 12 rolls of paper:
.......x..
.<b>@</b>@.x.x.<b>@</b>x
x@@@@...<b>@</b><b>@</b>
x.@@@@..x.
.<b>@</b>.@@@@.x.
.x@@@@@@.x
.x.@.@.@@<b>@</b>
..@@@.@@@@
.x<b>@</b>@@@@@@.
....@@@...

Remove 7 rolls of paper:
..........
.x<b>@</b>.....x.
.<b>@</b>@@@...xx
..@@@@....
.x.@@@@...
..<b>@</b>@@@@@..
...@.@.@@x
..<b>@</b>@@.@@@<b>@</b>
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:
..........
..x.......
.x<b>@</b>@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@<b>@</b>.
....@@@...

Remove 2 rolls of paper:
..........
..........
..x@@.....
..<b>@</b>@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...

Remove 1 roll of paper:
..........
..........
...<b>@</b>@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
...x<b>@</b>.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
....x.....
...<b>@</b>@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
</code></pre>
<p>Stop once no more rolls of paper are accessible by a forklift. In this example, a total of <code><b>43</b></code> rolls of paper can be removed.</p>
<p>Start with your original diagram. <b>How many rolls of paper in total can be removed by the Elves and their forklifts?</b></p>

<p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
<p>At this point, you should <a href="/2025">return to your Advent calendar</a> and try another puzzle.</p>
<p>If you still want to see it, you can <a href="4/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+%22Printing+Department%22+%2D+Day+4+%2D+Advent+of+Code+2025+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F4" target="_blank">Bluesky</a>
  <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Printing+Department%22+%2D+Day+4+%2D+Advent+of+Code+2025&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F4&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' && ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+%22Printing+Department%22+%2D+Day+4+%2D+Advent+of+Code+2025+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F4';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
