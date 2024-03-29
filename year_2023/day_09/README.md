
<h1>Day 9: Mirage Maintenance 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2023/day/9>Link to Day 9</a><h2>Part One 🎁</h2><p>You ride the camel through the sandstorm and stop where the ghost's maps told you to stop. <span title="The sound of a sandstorm slowly settling.">The sandstorm subsequently subsides, somehow seeing you standing at an <b>oasis</b>!</span></p>
<p>The camel goes to get some water and you stretch your neck. As you look up, you discover what must be yet another giant floating island, this one made of metal! That must be where the <b>parts to fix the sand machines</b> come from.</p>
<p>There's even a <a href="https://en.wikipedia.org/wiki/Hang_gliding" target="_blank">hang glider</a> partially buried in the sand here; once the sun rises and heats up the sand, you might be able to use the glider and the hot air to get all the way up to the metal island!</p>
<p>While you wait for the sun to rise, you admire the oasis hidden here in the middle of Desert Island. It must have a delicate ecosystem; you might as well take some ecological readings while you wait. Maybe you can report any environmental instabilities you find to someone so the oasis can be around for the next sandstorm-worn traveler.</p>
<p>You pull out your handy <b>Oasis And Sand Instability Sensor</b> and analyze your surroundings. The OASIS produces a report of many values and how they are changing over time (your puzzle input). Each line in the report contains the <b>history</b> of a single value. For example:</p>
<pre><code>0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
</code></pre>
<p>To best protect the oasis, your environmental report should include a <b>prediction of the next value</b> in each history. To do this, start by making a new sequence from the <b>difference at each step</b> of your history. If that sequence is <b>not</b> all zeroes, repeat this process, using the sequence you just generated as the input sequence. Once all of the values in your latest sequence are zeroes, you can extrapolate what the next value of the original history should be.</p>
<p>In the above dataset, the first history is <code>0 3 6 9 12 15</code>. Because the values increase by <code>3</code> each step, the first sequence of differences that you generate will be <code>3 3 3 3 3</code>. Note that this sequence has one fewer value than the input sequence because at each step it considers two numbers from the input. Since these values aren't <b>all zero</b>, repeat the process: the values differ by <code>0</code> at each step, so the next sequence is <code>0 0 0 0</code>. This means you have enough information to extrapolate the history! Visually, these sequences can be arranged like this:</p>
<pre><code>0   3   6   9  12  15
  3   3   3   3   3
    0   0   0   0
</code></pre>
<p>To extrapolate, start by adding a new zero to the end of your list of zeroes; because the zeroes represent differences between the two values above them, this also means there is now a placeholder in every sequence above it:<p>
<pre><code>0   3   6   9  12  15   <b>B</b>
  3   3   3   3   3   <b>A</b>
    0   0   0   0   <b>0</b>
</code></pre>
<p>You can then start filling in placeholders from the bottom up. <code>A</code> needs to be the result of increasing <code>3</code> (the value to its left) by <code>0</code> (the value below it); this means <code>A</code> must be <code><b>3</b></code>:</p>
<pre><code>0   3   6   9  12  15   B
  3   3   3   3   <b>3</b>   <b>3</b>
    0   0   0   0   <b>0</b>
</code></pre>
<p>Finally, you can fill in <code>B</code>, which needs to be the result of increasing <code>15</code> (the value to its left) by <code>3</code> (the value below it), or <code><b>18</b></code>:</p>
<pre><code>0   3   6   9  12  <b>15</b>  <b>18</b>
  3   3   3   3   3   <b>3</b>
    0   0   0   0   0
</code></pre>
<p>So, the next value of the first history is <code><b>18</b></code>.</p>
<p>Finding all-zero differences for the second history requires an additional sequence:</p>
<pre><code>1   3   6  10  15  21
  2   3   4   5   6
    1   1   1   1
      0   0   0
</code></pre>
<p>Then, following the same process as before, work out the next value in each sequence from the bottom up:</p>
<pre><code>1   3   6  10  15  21  <b>28</b>
  2   3   4   5   6   <b>7</b>
    1   1   1   1   <b>1</b>
      0   0   0   <b>0</b>
</code></pre>
<p>So, the next value of the second history is <code><b>28</b></code>.</p>
<p>The third history requires even more sequences, but its next value can be found the same way:</p>
<pre><code>10  13  16  21  30  45  <b>68</b>
   3   3   5   9  15  <b>23</b>
     0   2   4   6   <b>8</b>
       2   2   2   <b>2</b>
         0   0   <b>0</b>
</code></pre>
<p>So, the next value of the third history is <code><b>68</b></code>.</p>
<p>If you find the next value for each history in this example and add them together, you get <code><b>114</b></code>.</p>
<p>Analyze your OASIS report and extrapolate the next value for each history. <b>What is the sum of these extrapolated values?</b></p>

<p>To begin, <a href="9/input" target="_blank">get your puzzle input</a>.</p>
<form method="post" action="9/answer"><input type="hidden" name="level" value="1"/><p>Answer: <input type="text" name="answer" autocomplete="off"/> <input type="submit" value="[Submit]"/></p></form>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://twitter.com/intent/tweet?text=%22Mirage+Maintenance%22+%2D+Day+9+%2D+Advent+of+Code+2023&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2023%2Fday%2F9&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' && ms.length){this.href='https://'+ms+'/share?text=%22Mirage+Maintenance%22+%2D+Day+9+%2D+Advent+of+Code+2023+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2023%2Fday%2F9';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
