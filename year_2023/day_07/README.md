
<h1>Day 7: Camel Cards 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=https://adventofcode.com/2023/day/7>Link to Day 7</a><h2>Part One 🎁</h2><p>Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an <a href="https://en.wikipedia.org/wiki/Airship" target="_blank">airship</a>. (At least it's a <span title="Please only read this sentence while listening to 'The Airship Blackjack' from the Final Fantasy 6 soundtrack."><b>cool</b> airship</span>!) It drops you off at the edge of a vast desert and descends back to Island Island.</p>
<p>"Did you bring the parts?"</p>
<p>You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large <a href="https://en.wikipedia.org/wiki/Dromedary" target="_blank">camel</a>.</p>
<p>"Did you bring the parts?" she asks again, louder this time. You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.</p>
<p>"The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.</p>
<p>After riding a bit across the sands of Desert Island, you can see what look like very large rocks covering half of the horizon. The Elf explains that the rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there. Normally, they use big machines to move the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the <b>parts</b> they need to fix the machines.</p>
<p>You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help. You agree automatically.</p>
<p>Because the journey will take a few days, she offers to teach you the game of <b>Camel Cards</b>. Camel Cards is sort of similar to <a href="https://en.wikipedia.org/wiki/List_of_poker_hands" target="_blank">poker</a> except it's designed to be easier to play while riding a camel.</p>
<p>In Camel Cards, you get a list of <b>hands</b>, and your goal is to order them based on the <b>strength</b> of each hand. A hand consists of <b>five cards</b> labeled one of <code>A</code>, <code>K</code>, <code>Q</code>, <code>J</code>, <code>T</code>, <code>9</code>, <code>8</code>, <code>7</code>, <code>6</code>, <code>5</code>, <code>4</code>, <code>3</code>, or <code>2</code>. The relative strength of each card follows this order, where <code>A</code> is the highest and <code>2</code> is the lowest.</p>
<p>Every hand is exactly one <b>type</b>. From strongest to weakest, they are:</p>
<ul>
<li><b>Five of a kind</b>, where all five cards have the same label: <code>AAAAA</code></li>
<li><b>Four of a kind</b>, where four cards have the same label and one card has a different label: <code>AA8AA</code></li>
<li><b>Full house</b>, where three cards have the same label, and the remaining two cards share a different label: <code>23332</code></li>
<li><b>Three of a kind</b>, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: <code>TTT98</code></li>
<li><b>Two pair</b>, where two cards share one label, two other cards share a second label, and the remaining card has a third label: <code>23432</code></li>
<li><b>One pair</b>, where two cards share one label, and the other three cards have a different label from the pair and each other: <code>A23A4</code></li>
<li><b>High card</b>, where all cards' labels are distinct: <code>23456</code></li>
</ul>
<p>Hands are primarily ordered based on type; for example, every <b>full house</b> is stronger than any <b>three of a kind</b>.</p>
<p>If two hands have the same type, a second ordering rule takes effect. Start by comparing the <b>first card in each hand</b>. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the <b>same label</b>, however, then move on to considering the <b>second card in each hand</b>. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.</p>
<p>So, <code>33332</code> and <code>2AAAA</code> are both <b>four of a kind</b> hands, but <code>33332</code> is stronger because its first card is stronger. Similarly, <code>77888</code> and <code>77788</code> are both a <b>full house</b>, but <code>77888</code> is stronger because its third card is stronger (and both hands have the same first and second card).</p>
<p>To play Camel Cards, you are given a list of hands and their corresponding <b>bid</b> (your puzzle input). For example:</p>
<pre><code>32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
</code></pre>
<p>This example shows five hands; each hand is followed by its <b>bid</b> amount. Each hand wins an amount equal to its bid multiplied by its <b>rank</b>, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.</p>
<p>So, the first step is to put the hands in order of strength:</p>
<ul>
<li><code>32T3K</code> is the only <b>one pair</b> and the other hands are all a stronger type, so it gets rank <b>1</b>.</li>
<li><code>KK677</code> and <code>KTJJT</code> are both <b>two pair</b>. Their first cards both have the same label, but the second card of <code>KK677</code> is stronger (<code>K</code> vs <code>T</code>), so <code>KTJJT</code> gets rank <b>2</b> and <code>KK677</code> gets rank <b>3</b>.</li>
<li><code>T55J5</code> and <code>QQQJA</code> are both <b>three of a kind</b>. <code>QQQJA</code> has a stronger first card, so it gets rank <b>5</b> and <code>T55J5</code> gets rank <b>4</b>.</li>
</ul>
<p>Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (<code>765</code> * 1 + <code>220</code> * 2 + <code>28</code> * 3 + <code>684</code> * 4 + <code>483</code> * 5). So the <b>total winnings</b> in this example are <code><b>6440</b></code>.</p>
<p>Find the rank of every hand in your set. <b>What are the total winnings?</b></p>

<p>To begin, <a href="7/input" target="_blank">get your puzzle input</a>.</p>
<form method="post" action="7/answer"><input type="hidden" name="level" value="1"/><p>Answer: <input type="text" name="answer" autocomplete="off"/> <input type="submit" value="[Submit]"/></p></form>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://twitter.com/intent/tweet?text=%22Camel+Cards%22+%2D+Day+7+%2D+Advent+of+Code+2023&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2023%2Fday%2F7&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' && ms.length){this.href='https://'+ms+'/share?text=%22Camel+Cards%22+%2D+Day+7+%2D+Advent+of+Code+2023+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2023%2Fday%2F7';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a
></span>]</span> this puzzle.</p>
