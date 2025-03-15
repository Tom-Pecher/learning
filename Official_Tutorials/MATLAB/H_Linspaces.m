
% MATLAB: MathWorks, OnRamp
% Section 7: Linspaces

% Create an evenly spaced row vector of values 5 to 8:
v1 = 5:8;

% Change the step size:
v2 = 0:2:20;

% If we know how many values we want (rather than the step size), we can use linspace:
v3 = linspace(0, 10, 6);

% To create linearly spaced column vectors, we can use the transpose operator:
v4 = linspace(0, 10, 6)';
