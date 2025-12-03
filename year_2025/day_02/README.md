
<h1>Day 2: Gift Shop 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2025/day/2>Link to Day 2</a><h2>Part One 🎁</h2><p>You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.</p>
<p>As you make your way through the <span title="They even sell lunch boxes and blue tents!">surprisingly extensive</span> selection, one of the clerks recognizes you and asks for your help.</p>
<p>As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?</p>
<p>They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:</p>
<pre><code>11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124</code></pre>
<p>(The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)</p>
<p>The ranges are separated by commas (<code>,</code>); each range gives its <b>first ID</b> and <b>last ID</b> separated by a dash (<code>-</code>).</p>
<p>Since the young Elf was just doing silly patterns, you can find the <b>invalid IDs</b> by looking for any ID which is made only of some sequence of digits repeated twice. So, <code>55</code> (<code>5</code> twice), <code>6464</code> (<code>64</code> twice), and <code>123123</code> (<code>123</code> twice) would all be invalid IDs.</p>
<p>None of the numbers have leading zeroes; <code>0101</code> isn't an ID at all. (<code>101</code> is a <b>valid</b> ID that you would ignore.)</p>
<p>Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:</p>
<ul>
<li><code>11-22</code> has two invalid IDs, <code><b>11</b></code> and <code><b>22</b></code>.</li>
<li><code>95-115</code> has one invalid ID, <code><b>99</b></code>.</li>
<li><code>998-1012</code> has one invalid ID, <code><b>1010</b></code>.</li>
<li><code>1188511880-1188511890</code> has one invalid ID, <code><b>1188511885</b></code>.</li>
<li><code>222220-222224</code> has one invalid ID, <code><b>222222</b></code>.</li>
<li><code>1698522-1698528</code> contains no invalid IDs.</li>
<li><code>446443-446449</code> has one invalid ID, <code><b>446446</b></code>.</li>
<li><code>38593856-38593862</code> has one invalid ID, <code><b>38593859</b></code>.</li>
<li>The rest of the ranges contain no invalid IDs.</li>
</ul>
<p>Adding up all the invalid IDs in this example produces <code><b>1227775554</b></code>.</p>
<p><b>What do you get if you add up all of the invalid IDs?</b></p>

<h2>Part Two 🎁</h2><p>The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?</p>
<p>Now, an ID is invalid if it is made only of some sequence of digits repeated <b>at least</b> twice. So, <code>12341234</code> (<code>1234</code> two times), <code>123123123</code> (<code>123</code> three times), <code>1212121212</code> (<code>12</code> five times), and <code>1111111</code> (<code>1</code> seven times) are all invalid IDs.</p>
<p>From the same example as before:</p>
<ul>
<li><code>11-22</code> still has two invalid IDs, <code><b>11</b></code> and <code><b>22</b></code>.</li>
<li><code>95-115</code> now has two invalid IDs, <code><b>99</b></code> and <code><b>111</b></code>.</li>
<li><code>998-1012</code> now has two invalid IDs, <code><b>999</b></code> and <code><b>1010</b></code>.</li>
<li><code>1188511880-1188511890</code> still has one invalid ID, <code><b>1188511885</b></code>.</li>
<li><code>222220-222224</code> still has one invalid ID, <code><b>222222</b></code>.</li>
<li><code>1698522-1698528</code> still contains no invalid IDs.</li>
<li><code>446443-446449</code> still has one invalid ID, <code><b>446446</b></code>.</li>
<li><code>38593856-38593862</code> still has one invalid ID, <code><b>38593859</b></code>.</li>
<li><code>565653-565659</code> now has one invalid ID, <code><b>565656</b></code>.</li>
<li><code>824824821-824824827</code> now has one invalid ID, <code><b>824824824</b></code>.</li>
<li><code>2121212118-2121212124</code> now has one invalid ID, <code><b>2121212121</b></code>.</li>
</ul>
<p>Adding up all the invalid IDs in this example produces <code><b>4174379265</b></code>.</p>
<p><b>What do you get if you add up all of the invalid IDs using these new rules?</b></p>

<p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
<p>At this point, you should <a href="/2025">return to your Advent calendar</a> and try another puzzle.</p>
<p>If you still want to see it, you can <a href="2/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+%22Gift+Shop%22+%2D+Day+2+%2D+Advent+of+Code+2025+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F2" target="_blank">Bluesky</a>
  <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Gift+Shop%22+%2D+Day+2+%2D+Advent+of+Code+2025&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F2&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' && ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+%22Gift+Shop%22+%2D+Day+2+%2D+Advent+of+Code+2025+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F2';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
