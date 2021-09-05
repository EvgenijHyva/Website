<template>
    <div>
        <vee-form 
            :validation-schema="schema" 
            @submit="register"
            :initial-values="userDefaultData">
            <div class="form-field name">
                <div>
                    <label for="name">Name</label>
                    <vee-field name="name" type="text"
                    placeholder="Enter you full name">                    
                    </vee-field>
                </div>
                <ErrorMessage name="name" class="error-message" />
            </div>
            <div class="form-field email">
                <div>
                    <label for="name">Email</label>
                    <vee-field name="email" type="email"
                    placeholder="Enter you email">                    
                    </vee-field>
                </div>
                <ErrorMessage name="email"  class="error-message" />
            </div>
            <div class="form-field first_name">
                <div>
                    <label for="first_name">Firstname</label>
                    <vee-field name="first_name" type="text"
                    placeholder="Enter your firstname">                    
                    </vee-field>
                </div>
                <ErrorMessage name="first_name"  class="error-message" />
            </div>
            <div class="form-field last_name">
                <div>
                    <label for="last_name">Lastname</label>
                    <vee-field name="last_name" type="text"
                    placeholder="Enter your lastname">                    
                    </vee-field>
                </div>
                <ErrorMessage name="last_name"  class="error-message" />
            </div>
            <div class="form-field phone">
                <div>
                    <label for="phone">Phone</label>
                    <vee-field name="phone" type="number"
                    placeholder="Enter your phone">                    
                    </vee-field>
                </div>
                <ErrorMessage name="phone"  class="error-message" />
            </div>
            <div class="form-field gender">
                <div>
                    <label for="gender">Gender</label>
                    <vee-field as="select" name="gender" >
                        <option value="D" disabled>----</option> 
                        <option value="M">Male</option> 
                        <option value="F">Female</option>               
                        <option value="T">Transgender</option>               
                        <option value="O">Other</option>
                        <option value="U">UFO</option>               
                    </vee-field>
                </div>
                <ErrorMessage name="gender"  class="error-message" />
            </div>
            <div class="form-field password">
                <div>
                    <label for="password">Password</label>
                    <vee-field name="password" type="password"
                    placeholder="Enter your password" 
                    :bails="false" v-slot="{ field, errors }">
                        <input placeholder="Enter your password"
                        v-bind="field" type="password">      
                        <div v-for="error in errors" :key="error">
                            {{error}}
                        </div>              
                    </vee-field>
                </div>
                <ErrorMessage name="password"  class="error-message" />
            </div>
            <div class="form-field confirm-password">
                <div>
                <label for="confirm_password">Confirm password</label>
                <vee-field name="confirm_password" type="password"
                placeholder="Confirm password">                    
                </vee-field>
                </div>
                <ErrorMessage name="confirm_password"  class="error-message" />
            </div>
            <div class="form-field tos">
                <div>
                <label for="tos">Accept terms of sercice</label>
                <vee-field name="tos" type="checkbox" value="1" />                    
                </div>
                <ErrorMessage name="tos"  class="error-message" />
                <button type="submit" class="outline" :disabled="reg_in_submission">
                    Submit form
                </button>
            </div>
        </vee-form>
    </div>
</template>

<script>

export default{
    name: "RegisterForm",
    data() {
        return {
            schema: {
                name: "required|min:3|max:150|alpha_spaces",
                email: "required|min:3|max:100|email",
                first_name: "min:2|max:150",
                last_name: "min:2|max:150",
                password: "required|min:8|max:50",
                confirm_password: "password_mismatch:@password",
                phone: "required|min_value:010000000|max_value:9999999999",
                gender: "required|exclude_gender:U,E,A,D",
                tos: "tos"
            },

            userDefaultData: {
                gender: "D",
            },

            reg_in_submission: false, // if request is processing
            reg_show_alert: false,
            reg_alert_msg: "Please wait! Your account is being created.",
        }
    },
     methods: {
        register(values) {
            // TODO 
            this.reg_show_alert = true;
            this.reg_in_submission = true;
            this.reg_alert_msg= "Please wait! Your account is being created.",
            // 
            this.reg_alert_msg = "Success! Your account has been created.";
            console.log(values);
        },
    }
}
</script>

<style scoped>
form {
    max-width: 800px;
    border: 1px solid var(--secondary-color);
    border-radius: 5px;
    padding: 5px;
    background-color: #91c0df;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='152' height='152' viewBox='0 0 152 152'%3E%3Cg fill-rule='evenodd'%3E%3Cg id='temple' fill='%23896805' fill-opacity='0.4'%3E%3Cpath d='M152 150v2H0v-2h28v-8H8v-20H0v-2h8V80h42v20h20v42H30v8h90v-8H80v-42h20V80h42v40h8V30h-8v40h-42V50H80V8h40V0h2v8h20v20h8V0h2v150zm-2 0v-28h-8v20h-20v8h28zM82 30v18h18V30H82zm20 18h20v20h18V30h-20V10H82v18h20v20zm0 2v18h18V50h-18zm20-22h18V10h-18v18zm-54 92v-18H50v18h18zm-20-18H28V82H10v38h20v20h38v-18H48v-20zm0-2V82H30v18h18zm-20 22H10v18h18v-18zm54 0v18h38v-20h20V82h-18v20h-20v20H82zm18-20H82v18h18v-18zm2-2h18V82h-18v18zm20 40v-18h18v18h-18zM30 0h-2v8H8v20H0v2h8v40h42V50h20V8H30V0zm20 48h18V30H50v18zm18-20H48v20H28v20H10V30h20V10h38v18zM30 50h18v18H30V50zm-2-40H10v18h18V10z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
div {
    flex-grow: 1;
}

.form-field {
    display: flex;
    flex-direction: column;
}

label {
    color: var(--on-primary);
    margin-right: 10px;
}
input {
    border-radius: 10px;
    margin: 5px 0 5px 0;
    padding: 5px;
}
option {
    color: orange;
}
select {
    letter-spacing: 0.15rem;
    border-bottom: 3px solid transparent;
    font-size: 15px;
    font-weight:lighter;
    border-width: 0;
    margin-right: auto;
    cursor: pointer;
    color: black;
    background: var(--select); 
}
.error-message {
    color:  var(--primary-variant);
}
.text {
    color: var(--primary-variant)
}
.text-alt {
    background: var(--help-text-background);
    padding: 5px;
    border-radius: 5px;
    margin: 3px;
}

</style>