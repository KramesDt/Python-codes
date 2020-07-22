$factorial = 1;
print ("input a number : ");
$num = <STDIN>;
@rng = (1..$num);
foreach $i (@rng)
	{ $factorial = $factorial * $i;
	}
print ("The Factorial of $num = $factorial\n");