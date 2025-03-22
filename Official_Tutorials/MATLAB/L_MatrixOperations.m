
% MATLAB: MathWorks, OnRamp
% Section 11: Matrix Modification

data = rand(4, 7)

% Perform matrix-wide operations:
x = data + 5

% Perform operations between matrices:
y = data + x

% Basic statistical operations also work:
max(data)

% Perform element-wise operations:
z = data .* x
