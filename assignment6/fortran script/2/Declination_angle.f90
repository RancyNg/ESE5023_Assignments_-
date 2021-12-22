module Declination_angle

implicit none

	integer::d
	real(8)::a,b,pi

contains
	subroutine calculate1()
	pi=3.14159265358979
	write(*,*) 'input the number of days since January 1st d'
	read(*,*) d

	b=COS(pi/180*(360/365.24)*(d+10)+(360/pi)*0.0167*SIN((pi/180*360/365.24)*(d-2)))

	a=(ASIN(SIN(-23.44*pi/180)*b))*180/pi
	
	end subroutine calculate1


end module Declination_angle
