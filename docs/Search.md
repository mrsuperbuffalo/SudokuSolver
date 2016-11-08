# The Search

The search will be very similar to several other searches. I doubt anything I
have will be original. As of now I need to develop several things. I think I
might implement several tings very similar to our project at DecisionVis. I will
want to create a several constraints in a sqlite database that I will parse and
use for creating constraints. The constraints will be used to confine the
possible options for the tree. The search will make choices for each cell and
deduce what to do next.


## Constraints

How will they be represented? I'm not sure. What follows below seems to just
be a regurgitation of the things I have been working on over the last several
months. I think I need to make it a little stricter.

What is a constraint?

* A constraint is something that limits the possible solutions of a problem.

How does the constraint limit the possible solutions of a problem?

* A constraint would limit the ability to make certain decisions. I am going to
  extend this by saying that some decisions are only limited if some criteria is
  met.

What is a decision?

* A decision is the smallest meaningful increment of state that has an impact on
  the solution.

What does it mean to limit possible decisions?

* Decisions are limited by whether or not it is able to be acted upon.

What does it mean to act on a decision?

* A decision is acted on by determining whether or not it is part of the
  accepted decisions of the search.



### Putting it together

A constraint holds decisions and limits what is decisions can be made by changing
the availability of a decision by changing the state of other decisions that
haven't made it into the solution. So what does that mean? A constraint must be
able to hold decisions and much react hitting its limit. A constraint would need
to be able to know when to apply limiting ability based on some of it's accepted
(possibly rejected state) decisions. I seem to be beating around the bush when
it comes to determining constraint limits. A constraint can attempt to limit
decisions by saying that at most or at least X of these decisions can be accepted.
I didn't want to write it in those terms in case I was limiting what a constraint
could cover. So how do constraints come together to limit a solution? I think I
should probably walk through


42758.19.
....326..
.5.9142..
28....3..
.4.3.5.1.
..8....29
..1649.8.
..285....
.64.71935









---Other stuff---


How would this be represented?

* A constraint can either be activated or not. It must also be able to tell if
  it is violated or not.

What must a constraint represent? A constraint will hold the valid options for
the constraint. If a constraint is violated we should log the state of the
search at that point. This history will hopefully be used to stop the search
from reaching that state again. A constraint will have a valid number of
options. Once that number falls outside of its acceptable bounds it is considered
violated.