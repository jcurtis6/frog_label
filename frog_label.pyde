size (512, 512)

fill (51, 199, 28) #green

mutant_x = 250

#base of head
ellipse (mutant_x, 200, 200, 100)
#mouth
fill (62, 71, 61)
ellipse (mutant_x, 215, 130, 50)

#eyes
frog = 20
eye_y = 175
fill (0, 0, 0)
ellipse (215, eye_y, frog, frog)
ellipse (285, eye_y, frog, frog)

#ears
noStroke()
ellipse (
