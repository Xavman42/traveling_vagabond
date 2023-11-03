"""Solve a multiple knapsack problem using a MIP solver."""
from ortools.linear_solver import pywraplp


#asfd
def multi_knapsack_mip(weights, values, bin_capacities):
    data = {}

    data['weights'] = weights
    data['values'] = values
    data['bin_capacities'] = bin_capacities

    assert len(data['weights']) == len(data['values'])
    data['num_items'] = len(data['weights'])
    data['all_items'] = range(data['num_items'])

    data['num_bins'] = len(data['bin_capacities'])
    data['all_bins'] = range(data['num_bins'])

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if solver is None:
        print('SCIP solver unavailable.')
        return

    # Variables.
    # x[i, b] = 1 if item i is packed in bin b.
    x = {}
    for i in data['all_items']:
        for b in data['all_bins']:
            x[i, b] = solver.BoolVar(f'x_{i}_{b}')

    # Constraints.
    # Each item is assigned to at most one bin.
    for i in data['all_items']:
        solver.Add(sum(x[i, b] for b in data['all_bins']) <= 1)

    # The amount packed in each bin cannot exceed its capacity.
    for b in data['all_bins']:
        solver.Add(
            sum(x[i, b] * data['weights'][i]
                for i in data['all_items']) <= data['bin_capacities'][b])

    # Objective.
    # Maximize total value of packed items.
    objective = solver.Objective()
    for i in data['all_items']:
        for b in data['all_bins']:
            objective.SetCoefficient(x[i, b], data['values'][i])
    objective.SetMaximization()

    status = solver.Solve()

    bins = {}
    bins_packed_weight = {}
    bins_packed_value = {}
    if status == pywraplp.Solver.OPTIMAL:
        print(f'Total packed value: {objective.Value()}')
        total_weight = 0
        for b in data['all_bins']:
            print(f'Bin {b}')
            bin_weight = 0
            bin_value = 0
            bin_contents = []
            for i in data['all_items']:
                if x[i, b].solution_value() > 0:
                    print(
                        f"Item {i} weight: {data['weights'][i]} value: {data['values'][i]}"
                    )
                    bin_weight += data['weights'][i]
                    bin_value += data['values'][i]
                    bin_contents.append(data['values'][i])
            print(f'Packed bin weight: {bin_weight}')
            print(f'Packed bin value: {bin_value}\n')
            total_weight += bin_weight
            bins['bin_'+str(b)] = bin_contents
            bins_packed_value['bin_' + str(b) + '_value'] = bin_value
            bins_packed_weight['bin_' + str(b) + '_weight'] = bin_weight
        print(f'Total packed weight: {total_weight}')
        return bins, bins_packed_value, bins_packed_weight
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    my_weights = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ]
    my_values = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ]
    my_bin_capacities = [20, 20, 20, 20]
    bins = multi_knapsack_mip(my_weights, my_values, my_bin_capacities)
    print(bins)
