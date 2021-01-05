const { reverse, fibRec, fibDyn, fibIter, toStr } = require('./exercises.js');

describe.skip('reverse', () => {
  it('can reverse a simple string', () => {
    expect(reverse('hello')).toEqual('olleh');
  });

  it('can reverse a string with spaces', () => {
    expect(reverse('hello world')).toEqual('dlrow olleh');
  });

  it('can reverse a numeric string', () => {
    expect(reverse('123456789')).toEqual('987654321');
  });
});

describe.skip('fibRec', () => {
  it('given place, retursn the Fibonacci number', () => {
     expect(fibRec(10)).toEqual(55);
      expect(fibRec(1)).toEqual(1);
      expect(fibRec(0)).toEqual(0);
      expect(fibRec(20)).toEqual(6765);
  });
});

describe.skip('fibDyn', () => {
  it('given place, retursn the Fibonacci number', () => {
     expect(fibDyn(10)).toEqual(55);
      expect(fibDyn(1)).toEqual(1);
      expect(fibDyn(0)).toEqual(0);
      expect(fibDyn(20)).toEqual(6765);
  });
});

describe.skip('fibIter', () => {
  it('given place, retursn the Fibonacci number', () => {
     expect(fibIter(10)).toEqual(55);
      expect(fibIter(1)).toEqual(1);
      expect(fibIter(0)).toEqual(0);
      expect(fibIter(20)).toEqual(6765);
  });
});

describe.skip('toStr', () => {
  it('given number and base, converts number to string of that base', () => {
    expect(toStr(199, 10)).toEqual('199');
    expect(toStr(30, 1)).toEqual('11110');
  });
});
