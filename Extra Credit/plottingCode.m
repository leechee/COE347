clear
close all

dataForPlotting = importdata('u_vals_along_y.xlsx');
re10blox20 = dataForPlotting.U_Reynolds10_20blocks;
re10blox40 = dataForPlotting.U_Reynolds10_40blocks;
re10blox80 = dataForPlotting.U_Reynolds10_80blocks;
re10blox160 = dataForPlotting.U_Reynolds10_160blocks;

numb = median(re10blox20(:,4))/median(re10blox20(:,5));

figure()
plot(re10blox20(:,4), re10blox20(:,2), 'o')
hold on
plot(re10blox20(:,5)*10, re10blox20(:,2), '*')
title('Velocity with respect to position along the Y-direction at the center of the cavity (Position on Y-axis)')
subtitle('20x20 Grid Mesh')
legend('X-velocity', 'Y-velocity x 10')
xlabel('normalized velocity')
ylabel('Y-direction distance from bottom of cavity')

figure()
plot(re10blox40(:,4), re10blox40(:,2), 'o')
hold on
plot(re10blox40(:,5)*10, re10blox40(:,2), '*')
title('Velocity with respect to position along the Y-direction at the center of the cavity (Position on Y-axis)')
subtitle('40x40 Grid Mesh')
legend('X-velocity', 'Y-velocity x 10')
xlabel('normalized velocity')
ylabel('Y-direction distance from bottom of cavity')

figure()
plot(re10blox80(:,4), re10blox80(:,2), 'o')
hold on
plot(re10blox80(:,5)*10, re10blox80(:,2), '*')
title('Velocity with respect to position along the Y-direction at the center of the cavity (Position on Y-axis)')
subtitle('80x80 Grid Mesh')
legend('X-velocity', 'Y-velocity x 10')
xlabel('normalized velocity')
ylabel('Y-direction distance from bottom of cavity')

figure()
plot(re10blox160(:,4), re10blox160(:,2), 'o')
hold on
plot(re10blox160(:,5)*10, re10blox160(:,2), '*')
title('Velocity with respect to position along the Y-direction at the center of the cavity (Position on Y-axis)')
subtitle('160x160 Grid Mesh')
legend('X-velocity', 'Y-velocity x 10')
xlabel('normalized velocity')
ylabel('Y-direction distance from bottom of cavity')
%%
%comparing plots
figure()
plot(re10blox20(:,4), re10blox20(:,2), 'o', 'LineWidth',1.5)
hold on
plot(re10blox40(:,4), re10blox40(:,2), '*', 'LineWidth',1.5)
plot(re10blox80(:,4), re10blox80(:,2), '+', 'LineWidth',1.5)
plot(re10blox160(:,4), re10blox160(:,2), '.', 'LineWidth',1.5)
title('Velocity with respect to position along the Y-direction at the center of the cavity (Position on Y-axis)')
subtitle('X-velocity')
legend('20x20','40x40', '80x80', '160x160')
xlabel('normalized velocity')
ylabel('Y-direction distance from bottom of cavity')

figure()
plot(re10blox20(:,5), re10blox20(:,2), 'o', 'LineWidth',1.5)
hold on
plot(re10blox40(:,5), re10blox40(:,2), '*', 'LineWidth',1.5)
plot(re10blox80(:,5), re10blox80(:,2), '+', 'LineWidth',1.5)
plot(re10blox160(:,5), re10blox160(:,2), '.', 'LineWidth',1.5)
title('Velocity with respect to position along the Y-direction at the center of the cavity (Position on Y-axis)')
subtitle('Y-velocity')
legend('20x20','40x40', '80x80', '160x160')
xlabel('normalized velocity')
ylabel('Y-direction distance from bottom of cavity')