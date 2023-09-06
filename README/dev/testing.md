# Testing

@TODO

*Writing tests that never fail is a waste of time*

## Running all tests

Run

```shell
yarn test
```

## Where do I put my tests?

You just wrote a new fresh TypeScript module and want to test it? To do so, it depends on if you're going to

- Test a **non-page component** or any other TypeScript module 🤷: Create a module following the same path and with the `(...).test.tsx` extension.

- Test a **page component**: Create a module following the same path and with the `(...).test.tsx` extension, **but under `/src/pages.test/`**.

That's it 🎉, your tests are ready to run.
@TODO You will find examples in the source code of this project.

Before I forget, [why are you writing tests AFTER writing the source code](https://en.wikipedia.org/wiki/Test-driven_development)⁉️

## Documentation

Probably 90% of your questions regarding testing will be answered by:

- [Testing React](https://testing-library.com/docs/react-testing-library/intro/): You want to test a React component.

- [Testing React + OpenAPI](https://dev.to/epilot/testing-react-with-jest-and-openapi-mocks-8gc): How to test a React component that calls the back-end. **This decision is yet to be validated.**

- [Testing in general](https://jestjs.io/docs/getting-started): You have questions regarding the testing framework, like "What do the `describe` or `it` functions even do?".

## Writing good tests

This section is high-level enough to apply to any project, we hope it'll make you a better tester.

### Test functionality, not implementation

Do not test the **inner working** of your code, test that your code delivers. It is better to have two bad functions that when composed cancel each other's errors, than having two perfectly fine functions composed incorrectly.

Applied to this project: test that components (which are functions) return the expected output for given inputs. Keep in mind that a component returns rendered content.

If `MyComponent` calls `myPrivateFunction`, test that `MyComponent` renders the expected content. Do not test that `myPrivateFunction` works correctly.

### Your source code should not know it is being tested

Stop if you ever feel the necessity of writing source code **only for the purpose of testing**. Classic examples are exporting a constant since you wanted to use the exact implementation in your test or using `testId` because something you wanted to test was impossible to query.

The solution will be different for each case, but there are two key questions you have to ask yourself:

- What am I testing?
- Should I write this test?

Usually, the answers will be:

- You were testing something different from what you thought you were testing.
- You should not be testing that.

### Test how it works, not how it looks

Do not start by testing whether the rendered color of the button is the expected one. First, test the button:

- Is visible,
- Is clickable,
- It does what it should when clicked.

What we should care about is that our end-user can click the button and that the action triggered by that click work correctly. Then, and only then, if you consider the color an essential part of the contract of the component (generally, that's not the case), you can test the rendered color is the expected one. The same applies to most styling/positional properties, testing "this should be on the left" is generally a bad idea.

### `it('...')` should be self-explanatory

When writing a test, we want it to be self-explanatory. We should understand ~90% of of a test just by reading it. Do not aim for [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) or encapsulation when writing tests. Aim for readability of the isolated test. The "it" statement has to be explicit and clear. I should not need to scroll up to understand what the test was doing.

And please, [avoid nesting when you're testing](https://kentcdodds.com/blog/avoid-nesting-when-youre-testing).

### Mock only what is not part of your project

Your tests are not written for the pleasure of seing green. Your tests are written so that if someone changes something that breaks an expected functionality, they fail. If you mock parts of your codebase, or direct dependencies, the test might pass even when the functionality it was supposed to test is now broken.

### Do not write end-to-end tests

End-to-end tests (e2e) usually require complex setups and will likely break in _flaky_ ways due to factors that do not depend on the application itself. In this project, we avoid end-to-end tests altogether.
