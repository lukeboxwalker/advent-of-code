
<h1>Day 1: Calorie Counting 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2022/day/1>Link to Day 1</a><h2>Part One 🎁</h2>
<p>The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of <b>Calories</b> each Elf is carrying (your puzzle input).</p>
<p>The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, <span title="By &quot;etc&quot;, you're pretty sure they just mean &quot;more snacks&quot;.">etc.</span> that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.</p>
<p>For example, suppose the Elves finish writing their items' Calories and end up with the following list:</p>
<pre><code>1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
</code></pre>
<p>This list represents the Calories of the food carried by five Elves:</p>
<ul>
<li>The first Elf is carrying food with <code>1000</code>, <code>2000</code>, and <code>3000</code> Calories, a total of <code><b>6000</b></code> Calories.</li>
<li>The second Elf is carrying one food item with <code><b>4000</b></code> Calories.</li>
<li>The third Elf is carrying food with <code>5000</code> and <code>6000</code> Calories, a total of <code><b>11000</b></code> Calories.</li>
<li>The fourth Elf is carrying food with <code>7000</code>, <code>8000</code>, and <code>9000</code> Calories, a total of <code><b>24000</b></code> Calories.</li>
<li>The fifth Elf is carrying one food item with <code><b>10000</b></code> Calories.</li>
</ul>
<p>In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the <b>most</b> Calories. In the example above, this is <b><code>24000</code></b> (carried by the fourth Elf).</p>
<p>Find the Elf carrying the most Calories. <b>How many total Calories is that Elf carrying?</b></p>

<h2>Part Two 🎁</h2><p>By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually <b>run out of snacks</b>.</p>
<p>To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the <b>top three</b> Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.</p>
<p>In the example above, the top three Elves are the fourth Elf (with <code>24000</code> Calories), then the third Elf (with <code>11000</code> Calories), then the fifth Elf (with <code>10000</codE> Calories). The sum of the Calories carried by these three elves is <code><b>45000</b></code>.</p>
<p>Find the top three Elves carrying the most Calories. <b>How many Calories are those Elves carrying in total?</b></p>

