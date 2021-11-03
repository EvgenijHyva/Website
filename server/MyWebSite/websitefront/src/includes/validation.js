import { 
    Form as VeeForm, Field as VeeField, ErrorMessage, defineRule, configure 
} from "vee-validate";

import {
    required, min, max, alpha_spaces as aplhaSpaces, email, min_value as minVal,
    max_value as maxVal, confirmed, not_one_of as exclude, url
} from "@vee-validate/rules";


export default {
    install(app) {
        app.component("VeeForm", VeeForm);
        app.component("VeeField", VeeField);
        app.component("ErrorMessage", ErrorMessage);

        defineRule("required", required);
        defineRule("tos", required);
        defineRule("min", min);
        defineRule("max", max);
        defineRule("alpha_spaces", aplhaSpaces);
        defineRule("email", email);
        defineRule("min_value", minVal);
        defineRule("max_value", maxVal);
        defineRule("confirmed", confirmed);
        defineRule("password_mismatch", confirmed);
        defineRule("exclude", exclude);
        defineRule("exclude_gender", exclude);
        defineRule("url", url);
        
        configure({
            generateMessage: (context) => {
                const messages = {
                    required: `The field ${context.field} is required.`,
                    min: `The field ${context.field} is to short.`,
                    max: `The field ${context.field} is to long.`,
                    aplha_spaces: `the field ${context.field} may only contain alphabetical characters and spaces.`, 
                    email: `The field ${context.field} must be a valid email example: mail@post.domen`,
                    min_value: `The field ${context.field} is to low.`,
                    max_value: `The field ${context.field} is to high.`, 
                    confirmed: ``,
                    password_mismatch: `The passwords don't match.`,
                    exclude: `You are not alowwed to use this value for the field ${context.field}.`,
                    exclude_gender: `You are not alowed to use this value for gender selector.`,
                    tos: "You must accept Terms of Service.",
                    url: "Provide a valid website-link."
                };
                const message = messages[context.rule.name] ? 
                messages[context.rule.name] 
                : `The field ${context.field} is invalid.`;
                return message
            },
            validateOnBlur: true, //on blur event for less agressive behavier -> false
            validateOnChange: true,
            validateOnInput: false,
            validateOnModelUpdate: true, // if value changed in v-model derective
            
        });
    },
};