const nemo = ['nemo'];

function findNemo(array) {
    let t0 = performance.now()
    for (let i = 0; i < array.length; i++) {
        console.log('Found NEMO')
    }
    let t1 = performance.now();
    console.log('Call to find Nemo took' + (t1-t0 + 'milliseconds'));
}