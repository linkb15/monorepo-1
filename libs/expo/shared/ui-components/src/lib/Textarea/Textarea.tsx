import { Colors } from '@monorepo/expo/shared/static';
import { Control, Controller, ValidationValueMessage } from 'react-hook-form';
import {
  Platform,
  StyleProp,
  StyleSheet,
  Text,
  TextInput,
  View,
  ViewStyle,
} from 'react-native';

type TValidateFn = (
  data: unknown
) => boolean | string | Promise<boolean | string>;

type TRules = {
  required?: boolean | string | ValidationValueMessage<string>;
  min?: number | string | ValidationValueMessage<number | string>;
  max?: number | string | ValidationValueMessage<number | string>;
  maxLength?: number | string | ValidationValueMessage<number | string>;
  minLength?: number | string | ValidationValueMessage<number | string>;
  pattern?: RegExp | { value: RegExp; message: string };
  validate?:
    | TValidateFn
    | Record<string, TValidateFn>
    | { value: TValidateFn; message: string };
};

interface ITextareaProps {
  label: string;
  control: Control<any>;
  height?: 200;
  name: string;
  required?: boolean;
  disabled?: boolean;
  error?: boolean;
  rules?: TRules;
  componentStyle?: StyleProp<ViewStyle>;
}

export function Textarea(props: ITextareaProps) {
  const {
    label,
    control,
    rules,
    name,
    error,
    required,
    disabled,
    componentStyle,
    height = 200,
    ...rest
  } = props;
  return (
    <Controller
      control={control}
      name={name}
      render={({ field: { value, onBlur, onChange } }) => (
        <View style={[styles.TextareaContainer, componentStyle]}>
          {label && (
            <View style={styles.label}>
              <Text style={styles.labelText}>{label}</Text>
              {required && <Text style={styles.required}>*</Text>}
            </View>
          )}
          <View
            style={[
              styles.Textarea,
              {
                borderColor: error ? 'red' : Colors.DARK_BLUE,
              },
            ]}
          >
            <TextInput
              style={{
                color: disabled ? Colors.GRAY : 'black',
                paddingHorizontal: 16,
                fontFamily: 'Pragmatica-book',
                fontSize: 16,
                lineHeight: 24,
                height,
                ...Platform.select({
                  web: {
                    outline: 'none',
                  },
                }),
              }}
              multiline
              value={value}
              onBlur={onBlur}
              onChangeText={onChange}
              editable={!disabled}
              {...rest}
            />
          </View>
        </View>
      )}
    />
  );
}

const styles = StyleSheet.create({
  TextareaContainer: {
    position: 'relative',
    width: '100%',
    maxWidth: 600,
  },
  Textarea: {
    position: 'relative',
    backgroundColor: Colors.WHITE,
    borderWidth: 1,
    borderRadius: 3,
    justifyContent: 'center',
  },
  label: {
    flexDirection: 'row',
    marginBottom: 8,
  },
  labelText: {
    fontSize: 14,
    color: Colors.DARK_BLUE,
    textTransform: 'capitalize',
    fontFamily: 'Pragmatica-book',
  },
  required: {
    marginLeft: 2,
    color: 'red',
  },
});
