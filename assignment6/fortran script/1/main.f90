Program Main 

implicit none 

integer :: u,i,j 
real(4), dimension(5,3) :: M 
real(4), dimension(3,5) :: N 
real(4), dimension(5,5) :: MN

u=50

!M Matrix
open(unit=u, file='M.dat', status='old')

read(u,*)((M(i,j),j=1,3),i=1,5)

close(u)

!display
print*,'M'

do i=1,5 

	write(*,'(5f8.2)') M(i,:)

enddo 

!N Matrix
open(unit=u, file='N.dat', status='old') 

read(u,*)((N(i,j),j=1,5),i=1,3)

close(u)
 
!display
print*,'N'

do i=1,3

        write(*,'(5f8.2)') N(i,:)

enddo 

!call subroutine
call Matrix_multip(M, N, MN)

!display MN
print*,'MN'
write(*,'(5f8.2)') MN

!write MN.dat
open(unit=u, file='MN.dat', status='replace') 

do i=1,5

	write(u,'(f9.2,f9.2,f9.2,f9.2,f9.2)') MN(i,:) 

enddo 
close(u)

End Program Main
