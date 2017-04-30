% Earth-Moon system in normalized rotating frame
x = linspace(-1.5, 1.5, 1000);
y = linspace(-1.5, 1.5, 1000);
[X, Y] = meshgrid(x, y);
m1= 5.972e24; 
m2= 7.347e22;
a=m2/(m1+m2);
U = (1-a)./sqrt(Y.^2 + (X + a).^2) + ...
     a./sqrt(Y.^2 + (X + a - 1).^2) + ...
     0.5*(Y.^2 + X.^2);
Z = 2*U;%use jacobi constant to make graph clear
c = [1:0.05:5, 3.2:0.2:10];%tweak these for the plot
figure
contourf(X, Y, Z, c)
colorbar
