module Solar_hour_angle

	real(4)::h,LST

	contains 
        subroutine calculate2()

	write(*,*) 'input the local solar time (in minutes)  LST'
	read(*,*) LST

	h=15*((LST/60)-12)
	
	end subroutine calculate2
	
end module Solar_hour_angle
