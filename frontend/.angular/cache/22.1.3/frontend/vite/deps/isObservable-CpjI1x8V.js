import { wn as isFunction, xn as Observable } from "./operators-CZEcSKwx.js";
//#region node_modules/rxjs/dist/esm5/internal/util/isObservable.js
function isObservable(obj) {
	return !!obj && (obj instanceof Observable || isFunction(obj.lift) && isFunction(obj.subscribe));
}
//#endregion
export { isObservable as t };
