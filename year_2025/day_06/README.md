
<h1>Day 6: Trash Compactor 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2025/day/6>Link to Day 6</a><h2>Part One 🎁</h2><p>After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!</p>
<p>A brief fall later, you find yourself in a <span title="To your surprise, the smell isn't that bad.">garbage smasher</span>. Unfortunately, the door's been magnetically sealed.</p>
<p>As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her <a href="/2021/day/18">math homework</a>.</p>
<p>Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of <b>problems</b>; each problem has a group of numbers that need to be either <b>added</b> (<code>+</code>) or <b>multiplied</b> (<code>*</code>) together.</p>
<p>However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:</p>
<pre><code>123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
</code></pre>
<p>Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.</p>
<p>So, this worksheet contains four problems:</p>
<ul>
<li><code>123</code> * <code>45</code> * <code>6</code> = <code><b>33210</b></code></li>
<li><code>328</code> + <code>64</code> + <code>98</code> = <code><b>490</b></code></li>
<li><code>51</code> * <code>387</code> * <code>215</code> = <code><b>4243455</b></code></li>
<li><code>64</code> + <code>23</code> + <code>314</code> = <code><b>401</b></code></li>
</ul>
<p>To check their work, cephalopod students are given the <b>grand total</b> of adding together all of the answers to the individual problems. In this worksheet, the grand total is <code>33210</code> + <code>490</code> + <code>4243455</code> + <code>401</code> = <code><b>4277556</b></code>.</p>
<p>Of course, the actual worksheet is <b>much</b> wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.</p>
<p>Solve the problems on the math worksheet. <b>What is the grand total found by adding together all of the answers to the individual problems?</b></p>

<h2>Part Two 🎁</h2><p>The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.</p>
<p>Cephalopod math is written <b>right-to-left in columns</b>. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)</p>
<p>Here's the example worksheet again:</p>
<pre><code>123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
</code></pre>
<p>Reading the problems right-to-left one column at a time, the problems are now quite different:</p>
<ul>
<li>The rightmost problem is <code>4</code> + <code>431</code> + <code>623</code> = <code><b>1058</b></code></li>
<li>The second problem from the right is <code>175</code> * <code>581</code> * <code>32</code> = <code><b>3253600</b></code></li>
<li>The third problem from the right is <code>8</code> + <code>248</code> + <code>369</code> = <code><b>625</b></code></li>
<li>Finally, the leftmost problem is <code>356</code> * <code>24</code> * <code>1</code> = <code><b>8544</b></code></li>
</ul>
<p>Now, the grand total is <code>1058</code> + <code>3253600</code> + <code>625</code> + <code>8544</code> = <code><b>3263827</b></code>.</p>
<p>Solve the problems on the math worksheet again. <b>What is the grand total found by adding together all of the answers to the individual problems?</b></p>

<p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
<p>At this point, you should <a href="/2025">return to your Advent calendar</a> and try another puzzle.</p>
<p>If you still want to see it, you can <a href="6/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+%22Trash+Compactor%22+%2D+Day+6+%2D+Advent+of+Code+2025+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F6" target="_blank">Bluesky</a>
  <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Trash+Compactor%22+%2D+Day+6+%2D+Advent+of+Code+2025&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F6&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' && ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+%22Trash+Compactor%22+%2D+Day+6+%2D+Advent+of+Code+2025+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F6';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
