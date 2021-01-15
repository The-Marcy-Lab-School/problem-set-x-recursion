const { reverse, fibRec, fibIter, toStr } = require('./exercises.js');

describe('reverse', () => {
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

describe('fibIter', () => {
  it('given place, returns the Fibonacci number', () => {
      expect(fibIter(1)).toEqual(1);
      expect(fibIter(0)).toEqual(0);
      expect(fibIter(10)).toEqual(55);
      expect(fibIter(20)).toEqual(6765);
  });
});

describe('fibRec', () => {
  it('given place, returns the Fibonacci number', () => {
      expect(fibRec(1)).toEqual(1);
      expect(fibRec(0)).toEqual(0);
      expect(fibRec(10)).toEqual(55);
      expect(fibRec(20)).toEqual(6765);
  });
});

describe('toStr', () => {
  it('given number and base, converts number to string of that base', () => {
    expect(toStr(199, 10)).toEqual('199');
    expect(toStr(14, 8)).toEqual('16');
    expect(toStr(30, 2)).toEqual('11110');
  });
});
