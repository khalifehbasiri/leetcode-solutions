type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    const results: number[] = [];
    arr.forEach((x, i) => { Boolean(fn(x, i)) && results.push(x)})
    return results
};