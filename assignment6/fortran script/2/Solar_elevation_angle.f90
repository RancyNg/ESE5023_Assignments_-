program Solar_elevation_angle
   
use declination_angle
use solar_hour_angle      

implicit none   

real(4)::SEA,L

write(*,*)'input latitude L'
read(*,*) L

call calculate1()

call calculate2() 

SEA=(ASIN(SIN(L*pi/180)*SIN(a*pi/180)+COS(L*pi/180)*COS(a*pi/180)*COS(h*pi/180)))*180/pi

print*, "declination_angle = ",a
print*, "solar_hour_angle = ",h   
print*,"Solar_elevation_angle=",SEA
   
end program Solar_elevation_angle
