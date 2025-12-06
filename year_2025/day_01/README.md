
<h1>Day 1: Secret Entrance 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2025/day/1>Link to Day 1</a><h2>Part One 🎁</h2>
<p>You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the <b>password</b> seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:</p>
<p>"Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."</p>
<p>The safe has a dial with only an arrow on it; around the dial are the numbers <code>0</code> through <code>99</code> in order. As you turn the dial, it makes a small <b>click</b> noise as it reaches each number.</p>
<p>The attached document (your puzzle input) contains a sequence of <b>rotations</b>, one per line, which tell you how to open the safe. A rotation starts with an <code>L</code> or <code>R</code> which indicates whether the rotation should be to the <b>left</b> (toward lower numbers) or to the <b>right</b> (toward higher numbers). Then, the rotation has a <b>distance</b> value which indicates how many clicks the dial should be rotated in that direction.</p>
<p>So, if the dial were pointing at <code>11</code>, a rotation of <code>R8</code> would cause the dial to point at <code>19</code>. After that, a rotation of <code>L19</code> would cause it to point at <code>0</code>.</p>
<p>Because the dial is a circle, turning the dial <b>left from <code>0</code></b> one click makes it point at <code>99</code>. Similarly, turning the dial <b>right from <code>99</code></b> one click makes it point at <code>0</code>.</p>
<p>So, if the dial were pointing at <code>5</code>, a rotation of <code>L10</code> would cause it to point at <code>95</code>. After that, a rotation of <code>R5</code> could cause it to point at <code>0</code>.</p>
<p>The dial starts by pointing at <code>50</code>.</p>
<p>You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is <b>the number of times the dial is left pointing at <code>0</code> after any rotation in the sequence</b>.</p>
<p>For example, suppose the attached document contained the following rotations:</p>
<pre><code>L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
</code></pre>
<p>Following these rotations would cause the dial to move as follows:</p>
<ul>
<li>The dial starts by pointing at <code>50</code>.</li>
<li>The dial is rotated <code>L68</code> to point at <code>82</code>.</li>
<li>The dial is rotated <code>L30</code> to point at <code>52</code>.</li>
<li>The dial is rotated <code>R48</code> to point at <code><b>0</b></code>.</li>
<li>The dial is rotated <code>L5</code> to point at <code>95</code>.</li>
<li>The dial is rotated <code>R60</code> to point at <code>55</code>.</li>
<li>The dial is rotated <code>L55</code> to point at <code><b>0</b></code>.</li>
<li>The dial is rotated <code>L1</code> to point at <code>99</code>.</li>
<li>The dial is rotated <code>L99</code> to point at <code><b>0</b></code>.</li>
<li>The dial is rotated <code>R14</code> to point at <code>14</code>.</li>
<li>The dial is rotated <code>L82</code> to point at <code>32</code>.</li>
</ul>
<p>Because the dial points at <code>0</code> a total of three times during this process, the password in this example is <code><b>3</b></code>.</p>
<p>Analyze the rotations in your attached document. <b>What's the actual password to open the door?</b></p>

<h2>Part Two 🎁</h2><p>You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.</p>
<p>As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:</p>
<p>"Due to newer security protocols, please use <b>password method <span title="You should have seen the chaos when the Elves overflowed their 32-bit password method counter.">0x434C49434B</span></b> until further notice."</p>
<p>You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times <b>any click</b> causes the dial to point at <code>0</code>, regardless of whether it happens during a rotation or at the end of one.</p>
<p>Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:</p>
<ul>
<li>The dial starts by pointing at <code>50</code>.</li>
<li>The dial is rotated <code>L68</code> to point at <code>82</code>; during this rotation, it points at <code>0</code> <b>once</b>.</li>
<li>The dial is rotated <code>L30</code> to point at <code>52</code>.</li>
<li>The dial is rotated <code>R48</code> to point at <code><b>0</b></code>.</li>
<li>The dial is rotated <code>L5</code> to point at <code>95</code>.</li>
<li>The dial is rotated <code>R60</code> to point at <code>55</code>; during this rotation, it points at <code>0</code> <b>once</b>.</li>
<li>The dial is rotated <code>L55</code> to point at <code><b>0</b></code>.</li>
<li>The dial is rotated <code>L1</code> to point at <code>99</code>.</li>
<li>The dial is rotated <code>L99</code> to point at <code><b>0</b></code>.</li>
<li>The dial is rotated <code>R14</code> to point at <code>14</code>.</li>
<li>The dial is rotated <code>L82</code> to point at <code>32</code>; during this rotation, it points at <code>0</code> <b>once</b>.</li>
</ul>
<p>In this example, the dial points at <code>0</code> three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be <code><b>6</b></code>.</p>
<p>Be careful: if the dial were pointing at <code>50</code>, a single rotation like <code>R1000</code> would cause the dial to point at <code>0</code> ten times before returning back to <code>50</code>!</p>
<p>Using password method 0x434C49434B, <b>what is the password to open the door?</b></p>

<p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
<p>At this point, you should <a href="/2025">return to your Advent calendar</a> and try another puzzle.</p>
<p>If you still want to see it, you can <a href="1/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+%22Secret+Entrance%22+%2D+Day+1+%2D+Advent+of+Code+2025+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F1" target="_blank">Bluesky</a>
  <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Secret+Entrance%22+%2D+Day+1+%2D+Advent+of+Code+2025&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F1&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' && ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+%22Secret+Entrance%22+%2D+Day+1+%2D+Advent+of+Code+2025+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2025%2Fday%2F1';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
