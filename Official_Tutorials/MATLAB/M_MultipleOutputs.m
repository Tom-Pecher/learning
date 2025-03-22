
% MATLAB: MathWorks, OnRamp
% Section 12: Multiple Outputs

data = rand(4, 7)

% Perform matrix-wide operations:
[xsize, ysize] = size(data)

v = rand(1, 5)

% Obtain the index of important values:
[~, idx1] = max(v)

[vMin, idx2] = min(v)
